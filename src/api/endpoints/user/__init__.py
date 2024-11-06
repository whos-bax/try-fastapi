from typing import Union

from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.models import *
from core.database import get_db
from core.security import create_access_token

from service.user.schema import (
    LoginSchema
)

from service.user.layer import (
    UserServiceLayer
)

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/login")
async def login(
    login_form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user_email = login_form.username
    user_password = login_form.password
    login_schema = LoginSchema(email=user_email, password=user_password)
    return await UserServiceLayer.login(db, login_schema)