
from pathlib import Path

from app.rag.loader import load_document
from app.rag.chunker import split_into_chunks


def main():
    document_path = (
        Path(__file__).resolve().parents[1]
        / "documents"
        / "policies"
        / "health-policy.txt"
    )

    text = load_document(str(document_path))
    chunks = split_into_chunks(text)

    print(f"Document length: {len(text)} characters")
    print(f"Number of chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {index} ---")
        print(chunk)


if __name__ == "__main__":
    main()
