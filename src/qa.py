import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_question(paper_text, question):

    prompt = f"""
You are an AI Research Assistant.

Research Paper:
{paper_text[:15000]}

Question:
{question}

Answer only using information from the paper.

If the paper does not contain the answer,
reply:
"The paper does not provide this information."
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content