import os
from google import genai


def rank(query, components):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Missing GEMINI_API_KEY"

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an expert electronics sourcing engineer.

User query: {query}

Components:
{components}

Rules:
- Only use given components
- Pick best 3
- Explain why
- Mention sourcing advantages
- Be concise

Return clean readable output.
"""

        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"LLM Error: {e}"
