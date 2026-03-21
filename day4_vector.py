from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

# splitting
splitter = RecursiveCharacterTextSplitter(chunk_size =500, chunk_overlap=50)
with open("sample.txt","r") as f:
    text = f.read()

chunks = splitter.split_text(text)
# embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

embedding_chunks = model.encode(chunks)
embedding_query = model.encode("what is machine learning?")

# print(f"These are the the first 10 chunks: {embedding_chunks[0][:10]}")
# print(f"These are the first 10 embeded queries {embedding_query[:10]}")

# vectordb the chromadb
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("rag_collection")
collection.add(
    documents=chunks,
    embeddings=embedding_chunks.tolist(),
    ids=[f"chunks_{i}" for i in range(len(chunks))]
)
results = collection.query(
    query_embeddings=[embedding_query.tolist()],
    n_results=2
)

print(results["documents"][0])
