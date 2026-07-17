from src.embeddings import embeddings

vector = embeddings.embed_query("Artificial Intelligence")

print("Embedding length:", len(vector))