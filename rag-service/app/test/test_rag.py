from app.rag.pipeline import ask_question


question = "Does the policy cover acupuncture?"

answer = ask_question(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)