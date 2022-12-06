from datetime import datetime

from app.infra.entities.posts import PostModel

import pytest


@pytest.fixture
def post_example():
    return PostModel(
        id=1,
        title="How to...",
        content="In today's post...",
        published=True,
        created_at=datetime(2020, 1, 1),
        updated_at=datetime(2020, 3, 1),
    )


def test_post_data_format_to_dictionary(post_example):
    assert post_example.dict() == {
        "id": 1,
        "title": "How to...",
        "content": "In today's post...",
        "published": True,
        "created_at": datetime(2020, 1, 1),
        "updated_at": datetime(2020, 3, 1),
    }
