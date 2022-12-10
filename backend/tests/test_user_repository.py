import pytest
from app.domain.models.user_model import UserModel
from app.infra.config.db_config import DBConnectionHandler
from app.infra.entities.users_entity import User
from app.infra.repo.user_repository import UserRepository
from faker import Faker
from pydantic import EmailStr  # pylint: disable=no-name-in-module

faker = Faker()


@pytest.fixture
def db_connection():
    return DBConnectionHandler()


@pytest.fixture
def user_repository():
    return UserRepository()


def test_insert_one_new_user(
    user_repository: UserRepository,  # pylint: disable=redefined-outer-name
    db_connection: DBConnectionHandler,  # pylint: disable=redefined-outer-name
) -> None:
    # Arrange
    name: str = faker.name()
    email: EmailStr = faker.email()
    password: str = faker.word()
    engine = db_connection.get_engine()

    # Act
    new_user: UserModel = user_repository.insert_one(
        name=name, email=email, password=password
    )
    query_user: User = engine.execute(
        f"SELECT * FROM users WHERE email = '{new_user.email}'"
    ).fetchone()
    engine.execute(f"DELETE FROM users WHERE email = '{new_user.email}'")

    # Assert
    assert new_user.name == query_user.name
    assert new_user.email == query_user.email
    assert new_user.password == query_user.password


def test_select_one_user_by_email(
    user_repository: UserRepository,  # pylint: disable=redefined-outer-name
    db_connection: DBConnectionHandler,  # pylint: disable=redefined-outer-name
) -> None:
    # Arrange
    name: str = faker.name()
    email: EmailStr = faker.email()
    password: str = faker.word()
    engine = db_connection.get_engine()

    # Act
    engine.execute(
        f"""
        INSERT INTO users (name, email, password)
        VALUES ('{name}', '{email}', '{password}')
    """
    )
    query_user: UserModel = user_repository.select_one(user_email=email)
    engine.execute(f"DELETE FROM users WHERE email = '{email}'")

    # Assert
    assert query_user.name == name
    assert query_user.email == email
    assert query_user.password == password
