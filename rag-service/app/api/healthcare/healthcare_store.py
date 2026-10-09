
import json
from pathlib import Path

from app.services.rag_service import RAGService
from app.vector_store.lancedb_store import LanceDBStore


rag_service = RAGService()


class HealthcareStore:
    def __init__(self, table_name: str):
        self.store = LanceDBStore(
            db_path=str(rag_service.root / "vector_db"),
            table_name=table_name,
        )
        self.embedding_service = rag_service.embedding_service

    def _rows(self) -> list[dict]:
        if self.store.table_name not in self.store.db.table_names():
            return []

        table = self.store.db.open_table(self.store.table_name)
        return table.to_arrow().to_pylist()

    def get_all(self) -> list[dict]:
        records = []

        for row in self._rows():
            try:
                records.append(json.loads(row["text"]))
            except (KeyError, TypeError, json.JSONDecodeError):
                continue

        return records

    def get(self, record_id: str) -> dict | None:
        for record in self.get_all():
            if record.get("id") == record_id:
                return record
        return None

    def create(self, record_id: str, data: dict) -> dict:
        if self.get(record_id) is not None:
            raise ValueError(f"Record '{record_id}' already exists")

        record = {"id": record_id, **data}
        self._save(record_id, record)
        return record

    def update(self, record_id: str, data: dict) -> dict | None:
        existing = self.get(record_id)

        if existing is None:
            return None

        record = {"id": record_id, **data}
        self.store.delete_by_source(record_id)
        self._save(record_id, record)
        return record

    def delete(self, record_id: str) -> bool:
        if self.get(record_id) is None:
            return False

        self.store.delete_by_source(record_id)
        return True

    def _save(self, record_id: str, record: dict) -> None:
        text = json.dumps(record, ensure_ascii=False)
        vectors = self.embedding_service.embed_texts([text])

        self.store.add_documents(
            chunks=[text],
            vectors=vectors,
            source=record_id,
        )
