import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_quiz(text):

    prompt = f"""
You are an expert professor.

Read the research paper carefully.

Generate EXACTLY 5 multiple choice questions.

Rules:
- Every question MUST be answerable directly from the paper.
- Do NOT make up facts.
- Only ONE option should be correct.
- The other three options should be realistic but incorrect.
- The correct letter MUST exactly match the correct option.
- Do NOT include explanations.
- Do NOT output anything except the quiz.

Output format:

Q1|Question|A) Option|B) Option|C) Option|D) Option|A
Q2|Question|A) Option|B) Option|C) Option|D) Option|C
Q3|Question|A) Option|B) Option|C) Option|D) Option|D
Q4|Question|A) Option|B) Option|C) Option|D) Option|B
Q5|Question|A) Option|B) Option|C) Option|D) Option|A

Research Paper:
{text[:5000]}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1
    )

    return response.choices[0].message.content