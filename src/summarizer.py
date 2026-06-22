import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_summary(text):

    prompt = f"""
    Summarize this research paper.

    Include:
    1. Objective
    2. Methodology
    3. Results
    4. Conclusion

    Research Paper:

    {text[:15000]}
    """

    response = model.generate_content(prompt)

    return response.text