from datetime import datetime

import pytest
from app.infra.entities.users import UserModel


@pytest.fixture
def user_example():
    return UserModel(
        id=1,
        name="Mark",
        email="mark@mail.com",
        password="123",
        created_at=datetime(2020, 1, 1),
    )


def test_user_data_format_to_dictionary(user_example):
    assert user_example.dict() == {
        "id": 1,
        "name": "Mark",
        "email": "mark@mail.com",
        "password": "123",
        "created_at": datetime(2020, 1, 1),
    }
