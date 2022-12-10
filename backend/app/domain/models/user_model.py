from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr  # pylint: disable=no-name-in-module


class UserModel(BaseModel):
    """User data format"""

    id: Optional[int]
    name: str
    email: EmailStr
    password: str
    created_at: Optional[datetime]
