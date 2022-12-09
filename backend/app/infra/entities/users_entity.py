from datetime import datetime
from typing import Optional

from app.infra.config.db_base_config import Base
from pydantic import BaseModel, EmailStr  # pylint: disable=no-name-in-module
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func


class User(Base):
    """Users entity"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String(16), nullable=False)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    # id_post = relationship("Post")  # type: ignore

    def __repr__(self) -> str:
        return f"""
            <User(name={self.name},
            email={self.email},
            password={self.password})>
            """


class UserModel(BaseModel):
    """User data format"""

    id: Optional[int]
    name: str
    email: EmailStr
    password: str
    created_at: Optional[datetime]
