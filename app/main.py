import streamlit as st
import fitz

st.set_page_config(
    page_title="AI Research Paper Assistant",
    page_icon="📚"
)

st.title("📚 AI Research Paper Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    st.success("PDF processed successfully!")

    st.subheader("Extracted Text")

    st.text_area(
        "Paper Content",
        text[:5000],
        height=300
    )