from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct

client = QdrantClient(":memory:")

client.recreate_collection(
    collection_name="documents",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE,
    ),
)


def store_embeddings(chunks, embeddings):
    points = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        points.append(
            PointStruct(
                id=i,
                vector=embedding,
                payload={
                    "text": chunk
                }
            )
        )

    client.upsert(
        collection_name="documents",
        points=points
    )


def search(query_embedding, limit=3):
    results = client.query_points(
        collection_name="documents",
        query=query_embedding,
        limit=limit,
        with_payload=True,
    )

    return results.points