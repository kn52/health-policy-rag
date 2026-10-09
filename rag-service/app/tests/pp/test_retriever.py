from app.rag.retriever import retrieve


question = "Does the policy cover acupuncture?"

results = retrieve(question, top_k=2)

print(f"Results found: {len(results)}")

for index, result in enumerate(results, start=1):
    print("\n====================")
    print(f"Result: {index}")
    print(f"Source: {result['source']}")
    print(f"Distance: {result['_distance']}")
    print(result["text"])