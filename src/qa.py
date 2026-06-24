import os
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_question(paper_text, question):

    prompt = f"""
    You are an AI Research Assistant.

    Research Paper:
    {paper_text[:15000]}

    User Question:
    {question}

    Answer only using information from the paper.
    If the paper does not contain the answer,
    say:
    "The paper does not provide this information."
    """

    response = model.generate_content(prompt)

    return response.text