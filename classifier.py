import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

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
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content

