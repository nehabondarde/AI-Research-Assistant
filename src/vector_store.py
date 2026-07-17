from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.embeddings import embeddings
import shutil
import os


def create_vector_store(text):

    # Delete old database
    if os.path.exists("data/chroma_db"):
        shutil.rmtree("data/chroma_db")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    print(f"Total chunks: {len(chunks)}")

    db = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings
)

    return db