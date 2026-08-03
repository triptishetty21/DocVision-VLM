from fastapi import APIRouter, File, UploadFile

from app.services.file_service import save_uploaded_file
from app.services.pdf_service import pdf_to_images

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_info = save_uploaded_file(file)

    image_paths = pdf_to_images(file_info["file_path"])

    return {
        **file_info,
        "pages": len(image_paths),
        "images": image_paths,
    }