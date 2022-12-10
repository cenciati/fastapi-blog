from app.infra.config.db_base_config import Base
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

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.name == other.name
            and self.email == other.name
            and self.password == other.password
            and self.created_at == other.created_at
        )
