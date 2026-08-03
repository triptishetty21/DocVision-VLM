from fastapi import FastAPI

from app.api.upload import router as upload_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to DocVision-VLM 🚀"}


app.include_router(upload_router)