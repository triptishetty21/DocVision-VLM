from fastapi import APIRouter, File, UploadFile

from app.services.file_service import save_uploaded_file
from app.services.pdf_service import pdf_to_images
from app.services.ocr_service import extract_text
from app.services.chunk_service import chunk_document
from app.services.embedding_service import generate_embeddings
from app.services.vector_service import store_embeddings, search

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_info = save_uploaded_file(file)

    image_paths = pdf_to_images(file_info["file_path"])

    ocr_document = []

    for image in image_paths:
        page_text = extract_text(image)
        ocr_document.append(page_text)

    chunks = chunk_document(ocr_document)

    embeddings = generate_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return {
        **file_info,
        "pages": len(image_paths),
        "chunks": len(chunks),
        "message": "Document indexed successfully"
    }