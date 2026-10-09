
from pathlib import Path

from app.services.rag_service import RAGService


def main():
    root = Path(__file__).resolve().parents[1]

    policy_path = (
        root / "documents" / "policies" / "health-policy.txt"
    )

    rag_service = RAGService()

    count = rag_service.ingest_document(str(policy_path))
    print(f"Ingested {count} chunks.")

    question = "Does the plan cover acupuncture in Ohio?"
    results = rag_service.retrieve(question)

    print("\nRetrieved policy context:")

    for result in results:
        print(f"\nSource: {result['source']}")
        print(f"Distance: {result['distance']:.4f}")
        print(result["text"])


if __name__ == "__main__":
    main()
