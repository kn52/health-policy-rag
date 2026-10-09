
from fastapi import APIRouter, HTTPException

from .policy_models import PolicyCreate, PolicyUpdate
from app.rag.chunker import split_into_chunks
from app.services.rag_service import RAGService

router = APIRouter(
    prefix="/api/policies",
    tags=["Policies"],
)

rag_service = RAGService()


def get_policy_chunks(source: str) -> list[dict]:
    store = rag_service.store

    if store.table_name not in store.db.table_names():
        return []

    table = store.db.open_table(store.table_name)
    rows = table.to_arrow().to_pylist()

    return [
        {
            "id": row["id"],
            "text": row["text"],
            "source": row["source"],
        }
        for row in rows
        if row.get("source") == source
    ]


@router.post("")
def create_policy(request: PolicyCreate):
    if get_policy_chunks(request.source):
        raise HTTPException(
            status_code=409,
            detail="Policy already exists.",
        )

    chunks = split_into_chunks(request.content)

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="Policy content cannot be empty.",
        )

    vectors = rag_service.embedding_service.embed_texts(chunks)

    rag_service.store.add_documents(
        chunks=chunks,
        vectors=vectors,
        source=request.source,
    )

    return {
        "message": "Policy created successfully",
        "source": request.source,
        "chunks": len(chunks),
    }


@router.get("")
def list_policies():
    store = rag_service.store

    if store.table_name not in store.db.table_names():
        return {"policies": []}

    table = store.db.open_table(store.table_name)
    rows = table.to_arrow().to_pylist()

    policies = {}

    for row in rows:
        source = row.get("source")

        if not source:
            continue

        if source not in policies:
            policies[source] = {
                "source": source,
                "chunks": 0,
            }

        policies[source]["chunks"] += 1

    return {"policies": list(policies.values())}


@router.get("/{source}")
def get_policy(source: str):
    chunks = get_policy_chunks(source)

    if not chunks:
        raise HTTPException(
            status_code=404,
            detail="Policy not found.",
        )

    return {
        "source": source,
        "chunks": chunks,
    }


@router.put("/{source}")
def update_policy(source: str, request: PolicyUpdate):
    if not get_policy_chunks(source):
        raise HTTPException(
            status_code=404,
            detail="Policy not found.",
        )

    chunks = split_into_chunks(request.content)

    if not chunks:
        raise HTTPException(
            status_code=400,
            detail="Policy content cannot be empty.",
        )

    vectors = rag_service.embedding_service.embed_texts(chunks)

    rag_service.store.delete_by_source(source)

    rag_service.store.add_documents(
        chunks=chunks,
        vectors=vectors,
        source=source,
    )

    return {
        "message": "Policy updated successfully",
        "source": source,
        "chunks": len(chunks),
    }


@router.delete("/{source}")
def delete_policy(source: str):
    if not get_policy_chunks(source):
        raise HTTPException(
            status_code=404,
            detail="Policy not found.",
        )

    rag_service.store.delete_by_source(source)

    return {
        "message": "Policy deleted successfully",
        "source": source,
    }
