import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.pdf_processor import extract_text_from_pdf
from src.summarizer import generate_summary
from src.rag import rag_answer
from src.quiz_generator import generate_quiz


# ------------------------------
# Page Configuration
# ------------------------------

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)

# ------------------------------
# Sidebar
# ------------------------------

with st.sidebar:

    st.title("📚 AI Research Assistant")

    st.markdown("""
### Features

✅ Upload Research Papers

✅ AI Summary

✅ RAG Question Answering

✅ Quiz Generation

---

### Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Groq Llama 3.1

---

Developed by **Neha Bondarde**
""")

# ------------------------------
# Main Title
# ------------------------------

st.title("📚 AI Research Paper Assistant")

st.markdown("""
Upload a research paper in **PDF format** and let AI help you understand it.

### What this application can do

- 📝 Generate an AI Summary
- ❓ Answer questions using RAG
- 📚 Extract text from the paper
- 🧠 Generate an interactive quiz

---
""")

# ------------------------------
# Upload PDF
# ------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload Research Paper",
    type=["pdf"]
)

if uploaded_file:

    # Extract text
    text = extract_text_from_pdf(uploaded_file)

    # Generate Summary
    with st.spinner("🤖 Generating AI Summary..."):
        summary = generate_summary(text)

    st.header("📝 AI Summary")
    st.write(summary)

    st.divider()

    # ------------------------------
    # Question Answering
    # ------------------------------

    st.header("❓ Ask Questions About the Paper")

    question = st.text_input(
        "Enter your question"
    )

    if question:

        with st.spinner("🔍 Searching the paper..."):

            try:

                answer = rag_answer(
                    text,
                    question
                )

                st.subheader("Answer")
                st.success(answer)

            except Exception as e:

                st.error(f"QA Error: {e}")

    st.divider()

    # ------------------------------
    # View Extracted Paper
    # ------------------------------

    with st.expander("📄 View Extracted Paper"):

        st.text_area(
            "Extracted Text",
            text,
            height=400
        )

    st.divider()

    # ------------------------------
    # Quiz Generator
    # ------------------------------

    st.header("🧠 Quiz")

    if "quiz" not in st.session_state:
        st.session_state.quiz = None

    if st.button("Generate Quiz"):

        with st.spinner("📝 Creating Quiz..."):

            # Generate quiz from summary
            st.session_state.quiz = generate_quiz(summary)

    if st.session_state.quiz:

        questions = [
            q.strip()
            for q in st.session_state.quiz.split("\n")
            if q.strip()
        ]

        question_number = 1

        for q in questions:

            parts = q.split("|")

            if len(parts) == 7:

                question = parts[1]

                options = [
                    parts[2],
                    parts[3],
                    parts[4],
                    parts[5]
                ]

                correct = parts[6].strip().upper()

                st.subheader(f"Question {question_number}")

                user_answer = st.radio(
                    question,
                    options,
                    key=f"radio_{question_number}"
                )

                if st.button(
                    f"Check Answer {question_number}",
                    key=f"btn_{question_number}"
                ):

                    selected = user_answer.split(")")[0].strip().upper()

                    if selected == correct:

                        st.success("✅ Correct!")

                    else:

                        st.error(
                            f"❌ Incorrect.\n\nCorrect Answer: {correct}"
                        )

                st.divider()

                question_number += 1

# ------------------------------
# Footer
# ------------------------------

st.divider()

st.caption(
    "📚 AI Research Paper Assistant | Built using Streamlit, LangChain, ChromaDB, Groq & HuggingFace Embeddings"
)