import uuid
import enum as pyEnum
import os
from typing import Optional, Dict, Any

# sqlalchemy
from sqlalchemy import (
    String,
    DateTime,
    Boolean,
    ForeignKey,
    Float,
    Integer,
    select,
    Table,
    Column,
    Enum,
)
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy.sql import func, case
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.associationproxy import association_proxy, AssociationProxy
from sqlalchemy.sql.expression import text

from core.database import Base

class User(Base):
    __tablename__ = "user"
    email: Mapped[str] = mapped_column(
        String(128), unique=True, primary_key=True, index=True, nullable=True
    )
    username: Mapped[str] = mapped_column(String(128), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(128), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    affiliation: Mapped[str] = mapped_column(String(128), nullable=True)

    date_joined: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    last_login: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)