from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt as pyjwt
from .config import settings

app = FastAPI()
token_security = OAuth2PasswordBearer(tokenUrl=f"{settings.AUTH_SERVICE_URL}/login")

async def get_current_user(token: str = Depends(token_security)):
    auth_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate user",
        headers={"WWW-Authenticate": "Bearer"},
    )
    decoded_data = pyjwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
    username: str = decoded_data.get("sub")
    if username is None:
        raise auth_error
    return {"username": username}

@app.get("/health")
async def check_health():
    return {"status": "running"}

@app.get("/user")
async def get_user_info():
    return {"message": settings.SERVICE_NAME}

@app.get("/me")
async def view_my_profile(current_user: dict = Depends(get_current_user)):
    return current_user

@app.get("/")
async def home():
    return {"message": f"Hello from {settings.SERVICE_NAME}"}
