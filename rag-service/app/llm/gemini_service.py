import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-turbo")


def generate_answer(question: str, context: str) -> str:

    prompt = f"""
You are a health insurance policy assistant.

Answer the user's question using ONLY the policy context provided below.

If the answer is not available in the context, say:
"I could not find this information in the provided policy."

Do not make assumptions or invent information.

Policy Context:
{context}

User Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text