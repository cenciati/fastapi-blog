from app.domain.models.post_model import PostModel
from app.domain.models.user_model import UserModel
from app.infra.config.db_config import DBConnectionHandler
from app.infra.repo.post_repository import PostRepository
from app.infra.repo.user_repository import UserRepository
from faker import Faker
from pytest import fixture
from sqlalchemy.engine import Engine

faker = Faker()


@fixture(scope="function")
def engine() -> Engine:
    db_connection = DBConnectionHandler()
    return db_connection.get_engine()


@fixture(scope="function")
def user_model_example() -> UserModel:
    return UserModel(
        id=faker.pyint(),
        name=faker.name(),
        email=faker.email(),
        password=faker.password(),
        created_at=faker.date_time(),
    )


@fixture(scope="function")
def post_model_example() -> PostModel:
    return PostModel(
        id=faker.pyint(),
        title=faker.pystr(),
        content=faker.text(),
        published=faker.pybool(),
        created_at=faker.date_time(),
        updated_at=faker.date_time(),
    )


@fixture(scope="session")
def user_repository():
    return UserRepository()


@fixture(scope="session")
def post_repository():
    return PostRepository()
