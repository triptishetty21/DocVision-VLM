from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from qdrant_client.models import Filter

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

    results = client.search(
        collection_name="documents",
        query_vector=query_embedding,
        limit=limit,
    )

    return results