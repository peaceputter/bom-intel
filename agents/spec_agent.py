#import google.generativeai as genai
#from config import GEMINI_API_KEY

#genai.configure(api_key=GEMINI_API_KEY)
#model = genai.GenerativeModel("gemini-1.5-flash")

def extract_specs(query):
#    prompt = f"""
#Extract structured specs from this component query.

#Query: {query}

#Return JSON with:
#- category
#- power
#- voltage
#- interface
#- notes

#If unknown, keep null.
#"""

#    try:
#        response = model.generate_content(prompt).text
        return "response_text"
#    except Exception as e:
#        return f"Spec extraction error: {e}"
