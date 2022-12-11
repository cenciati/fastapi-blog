from abc import ABC, abstractmethod
from typing import Optional

from app.domain.models.user_model import UserModel
from pydantic import EmailStr  # pylint: disable=no-name-in-module


class UserRepositoryInterface(ABC):
    """Interface for user repository"""

    @classmethod
    @abstractmethod
    def insert_one(cls, name: str, email: EmailStr, password: str) -> UserModel:
        """Abstract class method"""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def select_one(
        cls, user_id: Optional[int] = None, user_email: Optional[EmailStr] = None
    ) -> UserModel:
        """Abstract class method"""
        raise NotImplementedError
