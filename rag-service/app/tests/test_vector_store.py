
from pathlib import Path

from app.rag.loader import load_document
from app.rag.chunker import split_into_chunks
from app.services.embedding_service import EmbeddingService
from app.vector_store.lancedb_store import LanceDBStore


def main():
    root = Path(__file__).resolve().parents[1]

    policy_path = (
        root / "documents" / "policies" / "health-policy.txt"
    )

    text = load_document(str(policy_path))
    chunks = split_into_chunks(text)

    embedding_service = EmbeddingService()
    vectors = embedding_service.embed_texts(chunks)

    store = LanceDBStore(
        db_path=str(root / "vector_db"),
        table_name="health_policy",
    )

    store.add_documents(
        chunks=chunks,
        vectors=vectors,
        source="health-policy.txt",
    )

    print(f"Stored {len(chunks)} policy chunks.")

    question = "Does the plan cover acupuncture in Ohio?"
    query_vector = embedding_service.embed_text(question)

    results = store.search(query_vector, limit=3)

    print("\nSearch results:")

    for result in results:
        print(f"\nSource: {result['source']}")
        print(f"Distance: {result['distance']:.4f}")
        print(f"Text: {result['text']}")


if __name__ == "__main__":
    main()
