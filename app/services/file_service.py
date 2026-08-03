from pathlib import Path
import shutil
import uuid

from fastapi import HTTPException, UploadFile

UPLOAD_DIR = Path("data/uploads")

def save_uploaded_file(file: UploadFile) -> dict:
    # Accept only PDFs
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Ensure upload directory exists
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    # Generate unique filename
    unique_filename = f"{uuid.uuid4()}.pdf"

    file_path = UPLOAD_DIR / unique_filename

    # Save file
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "original_filename": file.filename,
        "saved_filename": unique_filename,
        "file_path": str(file_path),
    }