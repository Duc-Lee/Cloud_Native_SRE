from fastapi import FastAPI
from .config import settings

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/order")
async def check_order():
    return {"message": settings.SERVICE_NAME}

@app.get("/")
async def index():
    return {"message": f"This is {settings.SERVICE_NAME}"}
