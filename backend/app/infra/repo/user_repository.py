from app.domain.models.user_model import UserModel
from app.infra.config.db_config import DBConnectionHandler
from app.infra.entities.users_entity import User
from pydantic import EmailStr  # pylint: disable=no-name-in-module


class UserRepository:
    """Manages user repository"""

    @classmethod
    def insert_one(cls, name: str, email: EmailStr, password: str) -> UserModel:
        """Insert data into user entity.

        Args:
            name (str): User name
            email (EmailStr): User email
            password (str): User password

        Return:
            User added model.
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(name=name, email=email, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()
                return UserModel(name=name, email=email, password=password)
            except Exception as exc:
                db_connection.session.rollback()
                raise ConnectionError from exc
            finally:
                db_connection.session.close()
