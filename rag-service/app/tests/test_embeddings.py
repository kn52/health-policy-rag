
from app.services.embedding_service import EmbeddingService


def main():
    embedding_service = EmbeddingService()

    text = (
        "Acupuncture may be covered at an authorized facility "
        "subject to plan conditions."
    )

    vector = embedding_service.embed_text(text)

    print("Embedding generated successfully")
    print("Vector dimensions:", len(vector))
    print("First five values:", vector[:5])


if __name__ == "__main__":
    main()
