import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def rewrite_query(user_query):
    prompt = f"""
You are an electronics engineer.

Convert the user query into a precise component search query.

Examples:
- "fast charging chip" → "USB PD controller 60W"
- "gaming RAM" → "LPDDR5 6400 8GB"

User query: {user_query}

Return ONLY the improved search query.
"""

    try:
        return model.generate_content(prompt).text.strip()
    except:
        return user_query
