import streamlit as st
import json
from datetime import datetime, timedelta
from src.decision import classifier, action_mapper
from src.value_extractor import extract_values

PROFILE_PATH = "data/profile.json"
DECISION_PATH = "data/decisions.json"

# -------------------------
# Helpers
# -------------------------

def load_profile():
    try:
        with open(PROFILE_PATH, "r") as f:
            return json.load(f)
    except:
        return {}

def save_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f)

def load_decisions():
    try:
        with open(DECISION_PATH, "r") as f:
            return [json.loads(line) for line in f]
    except:
        return []

def save_decisions(decisions):
    with open(DECISION_PATH, "w") as f:
        for d in decisions:
            f.write(json.dumps(d) + "\n")

# -------------------------
# Tabs
# -------------------------

tab1, tab2 = st.tabs(["New Decision", "Check Commitments"])

# =========================
# TAB 1 — NEW DECISION
# =========================

with tab1:

    profile = load_profile()

    # --- First time setup
    if "top_values" not in profile:

        st.header("Initial Setup")

        future_self = st.text_area(
            "What future version of you are you trying not to betray through your decisions?"
        )

        values = extract_values(future_self)

        if st.button("Save Profile"):

            profile = {
                "future_self": future_self,
                "top_values": values
            }

            save_profile(profile)
            st.success("Profile saved!")
            st.experimental_rerun()

        st.stop()

    # --- Situation Input
    st.header("Describe what you're stuck on")

    user_input = st.text_area("Situation")

    if st.button("Analyze Situation"):

        # -------------------------
        # USE YOUR EXISTING LOGIC
        # -------------------------
        block = classifier.classify_pattern(user_input)
        # -------------------------

        st.write(f"Detected Pattern: {block}")

        mode = st.radio(
            "Do you feel unsure what the best option is, \
             or are you struggling to act on what you believe is right?",
            [
                "Unsure what’s best",
                "Struggling to act"
            ]
        )

        # -------- OPTIMIZER MODE --------
        if mode == "Unsure what’s best":

            solution = action_mapper.get_suggested_action(block)

            st.subheader("Suggested Next Move")
            st.write(solution)

        # -------- COMMITMENT MODE --------
        if mode == "Struggling to act":

            st.subheader("Aligned Action Commitment")

            value = st.selectbox(
                "Which of your top values might this situation put at risk?",
                profile["top_values"]
            )

            aligned_action = st.text_input(
                "What is one action you can take in the next 48h \
                 that would express this value?"
            )

            if st.button("Commit to this action within 48h"):

                decision = {
                    "situation": user_input,
                    "block": block,
                    "value": value,
                    "aligned_action": aligned_action,
                    "committed_at": datetime.utcnow().isoformat(),
                    "due_by": (datetime.utcnow() + timedelta(hours=48)).isoformat(),
                    "status": "committed"
                }

                with open(DECISION_PATH, "a") as f:
                    f.write(json.dumps(decision) + "\n")

                st.success("Commitment recorded!")

# =========================
# TAB 2 — CHECK COMMITMENTS
# =========================

with tab2:

    st.header("Check Commitments")

    decisions = load_decisions()
    updated = False

    for i, d in enumerate(decisions):

        if d.get("status") == "committed":

            due = datetime.fromisoformat(d["due_by"])

            if datetime.utcnow() > due:

                st.subheader("Pending Commitment")
                st.write(f"Action: {d['aligned_action']}")

                acted = st.radio(
                    "Did you take the action?",
                    ["Yes", "No"],
                    key=f"acted_{i}"
                )

                if acted == "Yes":

                    alignment = st.slider(
                        "Did this feel aligned with who you want to become?",
                        1, 5,
                        key=f"align_{i}"
                    )

                    if st.button("Save Response", key=f"save_{i}"):

                        d["status"] = "acted"
                        d["alignment_rating"] = alignment
                        d["first_action_taken_at"] = datetime.utcnow().isoformat()

                        updated = True
                        st.success("Saved!")

                elif acted == "No":

                    if st.button("Mark as Missed", key=f"missed_{i}"):

                        d["status"] = "missed"
                        updated = True
                        st.warning("Marked as missed.")

    if updated:
        save_decisions(decisions)
