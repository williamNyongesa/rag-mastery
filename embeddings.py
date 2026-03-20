from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

splitters = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
with open("sample.txt","r")as f:
    text = f.read()

chunks = splitters.split_text(text)




model = SentenceTransformer("all-MiniLM-L6-v2")
chunks_embedding = model.encode(chunks)
query_embedding = model.encode("What is machine learning?")

# Print the first 10 numbers of chunks_embeddings[0]
# Print the first 10 numbers of query_embedding

print(f"Chunk 0 vector (first 10): {chunks_embedding[0][:10]}")
print(f"Query vector (first 10): {query_embedding[:10]}")




