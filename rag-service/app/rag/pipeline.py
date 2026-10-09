from app.rag.loader import load_txt
from app.rag.chunker import chunk_text
from app.services.embedding_service import generate_embedding
from app.vector_store.lancedb_store import create_table


from app.rag.retriever import retrieve
from app.llm.gemini_service import generate_answer


def ingest_document(file_path: str):
    # 1. Load document
    document = load_txt(file_path)

    # 2. Create chunks
    chunks = chunk_text(document["text"])

    records = []

    # 3. Generate embeddings
    for index, chunk in enumerate(chunks):
        vector = generate_embedding(chunk)

        records.append({
            "id": str(index),
            "text": chunk,
            "source": document["source"],
            "vector": vector
        })

    # 4. Store in LanceDB
    table = create_table("health_policy", records)

    return table



def ask_question(question: str) -> dict:

    results = retrieve(question, top_k=3)

    context_parts = []
    sources = []

    for result in results:

        context_parts.append(
            f"Source: {result['source']}\n"
            f"{result['text']}"
        )

        sources.append({
            "source": result["source"],
            "distance": result["_distance"]
        })

    context = "\n\n".join(context_parts)

    answer = generate_answer(question, context)

    return {
        "answer": answer,
        "sources": sources
    }