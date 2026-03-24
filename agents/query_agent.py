import os
from google import genai


def rewrite_query(user_query):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return user_query

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an electronics engineer.

Convert the user query into a precise component search query.

Examples:
- fast charging chip → USB PD controller 60W
- gaming RAM → LPDDR5 6400 8GB

User query: {user_query}

Return ONLY the improved search query.
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        return response.text.strip()

    except Exception:
        return user_query
