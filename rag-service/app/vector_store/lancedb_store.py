import lancedb


DB_PATH = "vector_db"


def get_db():
    return lancedb.connect(DB_PATH)


def create_table(name: str, data: list[dict]):
    db = get_db()

    if name in db.table_names():
        db.drop_table(name)

    return db.create_table(name, data=data)


def get_table(name: str):
    db = get_db()

    return db.open_table(name)