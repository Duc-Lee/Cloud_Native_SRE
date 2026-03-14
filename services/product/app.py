from fastapi import FastAPI
from .config import settings

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "good"}

@app.get("/product")
async def show_products():
    return {"message": settings.SERVICE_NAME}

@app.get("/")
async def root():
    return {"message": f"Hi from {settings.SERVICE_NAME}"}
