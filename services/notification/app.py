from fastapi import FastAPI
from .config import settings

app = FastAPI()

@app.get("/health")
async def status_check():
    return {"status": "ok"}

@app.get("/notification")
async def get_messages():
    return {"message": settings.SERVICE_NAME}

@app.get("/")
async def main():
    return {"message": f"Main page of {settings.SERVICE_NAME}"}
