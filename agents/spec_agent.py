import os
from google import genai


def extract_specs(query):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return {"error": "Missing GEMINI_API_KEY"}

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
Extract structured specs from this component query.

Query: {query}

Return JSON with:
- category
- size
- power
- voltage
- interface
- notes

If unknown, keep null.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return {"error": str(e)}
