from src.config import get_api_key

client = OpenAI(api_key=get_api_key())

def extract_values(future_self_text: str):

    prompt = f"""
A user is describing the kind of person they want to become.

Extract 5 core decision-guiding personal values implied in their description.

Only return values like:
Integrity, Courage, Autonomy, Authenticity, Compassion, Contribution,
Freedom, Stability, Growth, Creativity, Responsibility, Connection,
Excellence, Honesty, Independence, Discipline, Service, Truth

Return only a Python list of values.

User description:
\"\"\"{future_self_text}\"\"\"
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You extract decision-relevant personal values."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    raw = response.choices[0].message.content.strip()

    try:
        values = eval(raw)
    except:
        values = ["Integrity", "Growth", "Autonomy"]

    return values[:8]

