
from pathlib import Path


def load_document(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {path.resolve()}"
        )

    if path.suffix.lower() != ".txt":
        raise ValueError("Currently, only .txt files are supported.")

    text = path.read_text(encoding="utf-8").strip()

    if not text:
        raise ValueError("Document is empty.")

    return text
