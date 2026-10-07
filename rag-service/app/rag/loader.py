from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path: str) -> list[dict]:
    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            documents.append(
                {
                    "text": text.strip(),
                    "page": page_number,
                    "source": Path(file_path).name,
                }
            )

    return documents


def load_txt(file_path: str) -> dict:
    path = Path(file_path)

    text = path.read_text(encoding="utf-8")

    return {
        "text": text.strip(),
        "source": path.name
    }