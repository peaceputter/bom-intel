#import google.generativeai as genai
#from config import GEMINI_API_KEY

#genai.configure(api_key=GEMINI_API_KEY)

#model = genai.GenerativeModel("gemini-1.5-flash")

def rank(query, components):
#    prompt = f"""
#You are an expert electronics sourcing engineer.

#User query: {query}

#Components:
#{components}

#Rules:
#- Only use given components
#- Pick best 3
#- Explain why
#- Mention sourcing advantages
#- Be concise and practical

#Output clearly.
#"""

#    try:
#        response = model.generate_content(prompt)
        return "response_text"
#    except Exception as e:
#        return f"LLM Error: {e}"
