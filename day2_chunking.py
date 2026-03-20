from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("sample.txt", "r") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
chunks = splitter.split_text(text)

print(f"Text length: {len(text)}")
print(f"Number of chunks: {len(chunks)}")

print(f"splitted chunks are: {chunks}")
for i,k in enumerate(chunks):
    print(f"i is printed as {i} k is printed as {k}")
