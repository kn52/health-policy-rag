
import lancedb
import pyarrow as pa


class LanceDBStore:
    def __init__(
        self,
        db_path: str = "vector_db",
        table_name: str = "health_policy",
    ):
        self.db = lancedb.connect(db_path)
        self.table_name = table_name

        if table_name not in self.db.table_names():
            schema = pa.schema([
                pa.field("id", pa.string()),
                pa.field("text", pa.string()),
                pa.field("source", pa.string()),
                pa.field(
                    "vector",
                    pa.list_(pa.float32(), 384),
                ),
            ])

            self.db.create_table(
                table_name,
                schema=schema,
            )

    def add_documents(
        self,
        chunks: list[str],
        vectors: list[list[float]],
        source: str,
    ) -> None:
        if len(chunks) != len(vectors):
            raise ValueError(
                "The number of chunks must match the number of vectors."
            )

        if not chunks:
            return

        records = [
            {
                "id": f"{source}_{index}",
                "text": chunk,
                "source": source,
                "vector": vector,
            }
            for index, (chunk, vector) in enumerate(
                zip(chunks, vectors)
            )
        ]

        if self.table_name in self.db.table_names():
            table = self.db.open_table(self.table_name)
            table.add(records)
        else:
            self.db.create_table(
                self.table_name,
                data=records,
                schema=self.schema,
            )

    def search(
        self,
        query_vector: list[float],
        limit: int = 3,
    ) -> list[dict]:
        if self.table_name not in self.db.table_names():
            return []

        table = self.db.open_table(self.table_name)

        results = (
            table.search(query_vector)
            .limit(limit)
            .to_list()
        )

        return [
            {
                "text": result["text"],
                "source": result["source"],
                "distance": result["_distance"],
            }
            for result in results
        ]

    
    def delete_by_source(self, source: str) -> None:
        if self.table_name not in self.db.table_names():
            return

        table = self.db.open_table(self.table_name)

        # Escape single quotes for the LanceDB filter expression.
        safe_source = source.replace("'", "''")
        table.delete(f"source = '{safe_source}'")

