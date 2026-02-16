import streamlit as st
from main import get_next_move

st.set_page_config(page_title="Decision Support Tool")

st.title("LLM Decision Support Tool")
st.write("Move from anxious indecision to your next task-aligned action.")

user_input = st.text_area(
    "Describe what you're stuck on:",
    height=150
)

if st.button("Get Next Move"):

    if user_input:

        result = get_next_move(user_input)

        st.subheader("Detected Pattern")
        st.write(result["label"])

        st.subheader("Confidence")
        st.write(result["confidence"])

        st.subheader("Suggested Next Move")
        st.write(result["next_move"])

    else:
        st.warning("Please enter some text.")

