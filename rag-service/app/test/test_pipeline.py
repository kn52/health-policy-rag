from app.rag.pipeline import ingest_document


file_path = "documents/policies/health-policy.txt"

table = ingest_document(file_path)

print(f"Rows inserted: {table.count_rows()}")