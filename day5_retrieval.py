from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

with open("sample.txt", "r") as f:
    text = f.read()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(text)

model = SentenceTransformer("all-MiniLM-L6-v2")
embeding_chunks = model.encode(chunks)

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("rag_collection")
collection.add(
    documents=chunks,
    embeddings=embeding_chunks.tolist(),
    ids=[f"chunks_{i}" for i in range(len(chunks))]
)
def retrieve(query, k=3):
    query_embedding = model.encode(query)
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )

    return results["documents"][0]

query = input("Ask a question: ")
results = retrieve(query)
for i, chunk in enumerate(results):
    print(f"\nResult {i+1}:\n{chunk}")