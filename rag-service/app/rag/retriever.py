from app.embeddings.embedding_service import generate_embedding
from app.vector_store.lancedb_store import get_table


def retrieve(
    question: str,
    top_k: int = 3
) -> list[dict]:

    # Generate embedding for the question
    query_vector = generate_embedding(question)

    # Open LanceDB table
    table = get_table("health_policy")

    # Search for similar chunks
    results = (
        table.search(query_vector)
        .limit(top_k)
        .to_list()
    )

    return results