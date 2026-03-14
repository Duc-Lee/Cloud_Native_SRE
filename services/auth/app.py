from datetime import datetime, timedelta
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from .config import settings
import jwt as pyjwt
from passlib.context import CryptContext

app = FastAPI()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_security = OAuth2PasswordBearer(tokenUrl="login")

fake_db = {
    "admin": {
        "username": "admin",
        "full_name": "Admin User",
        "email": "admin@example.com",
        "hashed_password": password_context.hash("admin123"),
        "disabled": False,
    }
}

class TokenResult(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserInfo(BaseModel):
    username: str
    email: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(UserInfo):
    hashed_password: str

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)

def create_token(data_to_encode: dict, expire_time: Optional[timedelta] = None):
    data_copy = data_to_encode.copy()
    if expire_time:
        expire = datetime.utcnow() + expire_time
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    data_copy.update({"exp": expire})
    encoded_jwt = pyjwt.encode(data_copy, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

@app.get("/health")
async def check_health():
    return {"status": "ok"}

@app.post("/login", response_model=TokenResult)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    expire_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    new_token = create_token(
        data_to_encode={"sub": user["username"]}, expire_time=expire_delta
    )
    return {"access_token": new_token, "token_type": "bearer"}

@app.get("/auth")
async def get_auth_info():
    return {"message": settings.SERVICE_NAME}

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.SERVICE_NAME}"}
