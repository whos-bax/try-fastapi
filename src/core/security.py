from fastapi import HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from core.settings import settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain: str) -> str:
    return password_context.hash(plain)


def verify_password(plain: str, hashed: str) -> bool:
    return password_context.verify(plain, hashed)


class Token(BaseModel):
    # email: str
    access_token: str
    token_type: str


def create_access_token(email: str):
    expires_delta = timedelta(minutes=settings.access_token_expire_minutes)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"sub": email, "exp": expire}
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=settings.algorithm
    )
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        email: str = payload.get("sub")
        return email

    except:
        raise HTTPException(status_code=401, detail="Invalid token")