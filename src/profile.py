import json

PROFILE_PATH = "data/profile.json"

def save_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f)

def load_profile():
    try:
        with open(PROFILE_PATH, "r") as f:
            return json.load(f)
    except:
        return {}

def run_profile_setup(extract_values_fn, rank_values_fn, st):

    st.header("Identity Setup")

    future_self = st.text_area(
        "What future version of you are you trying not to betray through your decisions?"
    )

    values = st.multiselect(
        "Select up to 5 values",
        DEFAULT_VALUES,
        max_selections=5
    )

    if st.button("Save Profile"):

        profile = {
            "future_self": future_self,
            "top_values": values
        }

        save_profile(profile)
        st.success("Profile saved!")
        st.experimental_rerun()

