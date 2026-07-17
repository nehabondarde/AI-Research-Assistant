import os
from dotenv import load_dotenv
from groq import Groq
from src.vector_store import create_vector_store

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def rag_answer(text, question):

    print("########## RAG FUNCTION CALLED ##########")

    # Create vector database
    db = create_vector_store(text)

    # Retrieve relevant chunks
    docs = db.similarity_search(question, k=4)

    # Print retrieved chunks
    for i, doc in enumerate(docs):
        print(f"\n========== Chunk {i+1} ==========\n")
        print(doc.page_content)

    # Build context
    context = "\n\n".join(doc.page_content for doc in docs)

    print("\n================ CONTEXT ================\n")
    print(context)
    print("\n=========================================\n")

    prompt = f"""
You are an AI Research Assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}

If the answer is not present in the context, reply exactly:
"The paper does not provide this information."
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content