from fastapi import FastAPI
from .config import settings

app = FastAPI()

@app.get("/health")
async def live():
    return {"status": "alive"}

@app.get("/payment")
async def my_payment_info():
    return {"message": settings.SERVICE_NAME}

@app.get("/")
async def hello():
    return {"message": f"Hello from {settings.SERVICE_NAME}"}
