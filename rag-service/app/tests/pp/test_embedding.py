from app.services.embedding_service import generate_embedding


text = "The policy covers hospitalization expenses."

embedding = generate_embedding(text)

print(f"Embedding dimensions: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")