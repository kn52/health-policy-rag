from app.rag.loader import load_txt
from app.rag.chunker import chunk_text


file_path = "documents/policies/health-policy.txt"

document = load_txt(file_path)

chunks = chunk_text(document["text"])

print(f"Total chunks: {len(chunks)}")

for index, chunk in enumerate(chunks, start=1):
    print("\n--------------------")
    print(f"Chunk: {index}")
    print(chunk)