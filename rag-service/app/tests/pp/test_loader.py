from app.rag.loader import load_txt


file_path = "documents/policies/health-policy.txt"

document = load_txt(file_path)

print(f"Source: {document['source']}")
print("\n--------------------")
print(document["text"])