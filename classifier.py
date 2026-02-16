import json
from openai import OpenAI
import os
import streamlit as st

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
else:
    api_key = st.secrets["OPENAI_API_KEY"]

model = st.secrets["MODEL"]

client = OpenAI(api_key=api_key)

# Load taxonomy
with open("taxonomy.json", "r") as f:
    taxonomy = json.load(f)

labels = list(taxonomy.keys())

def classify_pattern(user_input):

    prompt = f"""
You are a cognitive pattern classifier.

Classify the main decision-blocking pattern in the text below.

Text:
"{user_input}"

Choose ONLY one label from:
{labels}

Return your answer as JSON in this exact format:
{{
  "label": "<label>",
  "confidence": <float between 0 and 1>
}}
"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)
