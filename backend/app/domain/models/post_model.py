from datetime import datetime
from typing import Optional

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class PostModel(BaseModel):
    """Post data format"""

    id: Optional[int]
    title: str
    content: str
    published: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
