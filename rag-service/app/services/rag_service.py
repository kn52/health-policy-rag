
from pathlib import Path

from app.rag.loader import load_document
from app.rag.chunker import split_into_chunks
from app.services.embedding_service import EmbeddingService
from app.vector_store.lancedb_store import LanceDBStore


class RAGService:
    def __init__(self):
        self.root = Path(__file__).resolve().parents[2]

        self.embedding_service = EmbeddingService()

        self.store = LanceDBStore(
            db_path=str(self.root / "vector_db"),
            table_name="health_policy",
        )

    def ingest_document(self, file_path: str) -> int:
        text = load_document(file_path)
        chunks = split_into_chunks(text)

        vectors = self.embedding_service.embed_texts(chunks)

        self.store.add_documents(
            chunks=chunks,
            vectors=vectors,
            source=Path(file_path).name,
        )

        return len(chunks)

    def retrieve(
        self,
        question: str,
        limit: int = 3,
    ) -> list[dict]:
        query_vector = self.embedding_service.embed_text(question)

        return self.store.search(
            query_vector=query_vector,
            limit=limit,
        )
    
    def reindex_document(self, file_path: str) -> int:
        path = Path(file_path)

        # Remove previously indexed chunks for this file.
        self.store.delete_by_source(path.name)

        # Load and split the latest file content.
        text = load_document(str(path))
        chunks = split_into_chunks(text)

        if not chunks:
            return 0

        # Generate embeddings for the updated chunks.
        vectors = self.embedding_service.embed_texts(chunks)

        # Save the updated chunks and vectors.
        self.store.add_documents(
            chunks=chunks,
            vectors=vectors,
            source=path.name,
        )

        return len(chunks)

