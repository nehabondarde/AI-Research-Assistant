import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.pdf_processor import extract_text_from_pdf
st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚"
)

st.title("📚 AI Research Paper Assistant")

st.write(
    "Upload a research paper and extract its contents."
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(
        uploaded_file
    )

    st.success("PDF processed successfully!")

    st.subheader("Extracted Text")

    st.text_area(
        "Paper Content",
        text[:5000],
        height=300
    )