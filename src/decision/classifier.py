import json
from openai import OpenAI
import os
import streamlit as st
from src.llm.client import get_client
from src.config import get_model

client = get_client()
MODEL = get_model()

# Load taxonomy
with open("data/taxonomy.json", "r") as f:
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
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)
