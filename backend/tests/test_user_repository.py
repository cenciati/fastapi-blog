import pytest
from app.infra.entities.users_entity import UserModel
from app.infra.repo.user_repository import UserRepository
from faker import Faker
from pydantic import EmailStr  # pylint: disable=no-name-in-module

faker = Faker()


@pytest.fixture
def user_repository():
    return UserRepository()


def test_insert_one_new_user(
    user_repository: UserRepository,  # pylint: disable=redefined-outer-name
) -> None:
    # Arrange
    name: str = faker.name()
    email: EmailStr = faker.email()
    password: str = faker.word()

    # Act
    new_user: UserModel = user_repository.insert_one(
        name=name, email=email, password=password
    )
    # query_user: UserModel = user_repository.select_one()

    # Assert
    assert new_user.name == name  # query_user.name
    assert new_user.email == email  # query_user.email
    assert new_user.password == password  # query_user.password
