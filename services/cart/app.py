from fastapi import FastAPI
from .config import settings

app = FastAPI()

@app.get("/health")
async def check_health():
    return {"status": "ok"}

@app.get("/cart")
async def get_my_cart():
    return {"message": settings.SERVICE_NAME}

@app.get("/")
async def welcome():
    return {"message": f"Welcome to {settings.SERVICE_NAME}"}
