from abc import ABC, abstractmethod
from typing import Optional

from app.domain.models.post_model import PostModel


class PostRepositoryInterface(ABC):
    """Interface for post repository"""

    @classmethod
    @abstractmethod
    def insert_one(
        cls, title: str, content: str, published: Optional[bool] = True
    ) -> PostModel:
        """Abstract class method"""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def select_one(
        cls, post_id: Optional[int] = None, post_title: Optional[str] = None
    ) -> PostModel:
        """Abstract class method"""
        raise NotImplementedError
