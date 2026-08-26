import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def generate_answer(question: str, context: list[str]):

    context_text = "\n\n".join(context)

    prompt = f"""
Answer the user's question using only the provided context.

Context:
{context_text}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="qwen/qwen3-30b-a3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content