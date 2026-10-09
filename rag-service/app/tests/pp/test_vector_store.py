from app.vector_store.lancedb_store import create_table, get_table


data = [
    {
        "id": "1",
        "text": "The policy covers hospitalization expenses.",
        "vector": [0.1, 0.2, 0.3]
    },
    {
        "id": "2",
        "text": "Acupuncture is covered at an authorized medical facility.",
        "vector": [0.4, 0.5, 0.6]
    }
]


table = create_table("health_policy", data)

print(f"Rows inserted: {table.count_rows()}")

table = get_table("health_policy")

print(f"Table name: {table.name}")