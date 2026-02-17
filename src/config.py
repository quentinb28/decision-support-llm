import os
import streamlit as st
from dotenv import load_dotenv

def get_api_key():
    load_dotenv()

    if "OPENAI_API_KEY" in os.environ:
        return os.environ["OPENAI_API_KEY"]

    return st.secrets["OPENAI_API_KEY"]


def get_model():
    load_dotenv()

    if "MODEL" in os.environ:
        return os.environ["MODEL"]

    return st.secrets["MODEL"]

