from sqlalchemy.orm import Session
from datetime import datetime, timezone
from fastapi import HTTPException

from core.models import *
from core.security import verify_password, hash_password, create_access_token
from service.user.schema import LoginSchema

class UserServiceLayer:
    @staticmethod
    async def login(db: Session, login_schema: LoginSchema):

        user = db.query(User).filter(User.email == login_schema.email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User Not Found")
        
        if not verify_password(login_schema.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid password")
        
        user.last_login = datetime.now(timezone.utc)
        db.commit()
        db.refresh(user)

        access_token = create_access_token(user.email)
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "username": user.username,
        }