from app.services.embedding_service import generate_embeddings
from app.services.vector_service import search


def retrieve_relevant_chunks(question: str, limit: int = 3):
    query_embedding = generate_embeddings([question])[0]

    results = search(
        query_embedding,
        limit=limit
    )

    return [result.payload["text"] for result in results]