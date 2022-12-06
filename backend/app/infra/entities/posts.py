from datetime import datetime

from app.infra.config.db_base import Base
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Post(Base):
    """Posts entity"""

    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), nullable=False, unique=True)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default="NOT YET")
    id_owner = relationship("User")  # type: ignore

    def __repr__(self) -> str:
        return f"""
            <Post(title={self.title},
            content={self.content})>
            """


class PostModel(BaseModel):
    """Post data format"""

    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    updated_at: datetime
