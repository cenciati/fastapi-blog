from app.infra.config.db_base_config import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func


class Post(Base):
    """Posts entity"""

    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False, unique=True)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default="TRUE")
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    # id_owner = relationship("User")  # type: ignore

    def __repr__(self) -> str:
        return f"""
            <Post(id={self.id},
            title={self.title},
            content={self.content},
            published={self.published},
            created_at={self.created_at})>
            """

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.title == other.title
            and self.content == other.content
            and self.published == other.published
            and self.created_at == other.created_at
        )
