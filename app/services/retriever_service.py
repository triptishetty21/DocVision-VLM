from app.services.embedding_service import generate_embeddings
from app.services.vector_service import search


def retrieve_relevant_chunks(query: str, top_k: int = 3):
    query_embedding = generate_embeddings([query])[0]

    results = search(
        query_embedding=query_embedding,
        limit=top_k
    )

    return results