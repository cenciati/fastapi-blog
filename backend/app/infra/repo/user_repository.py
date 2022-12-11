from typing import Optional

from app.data.interfaces.user_repository_interface import UserRepositoryInterface
from app.domain.models.user_model import UserModel
from app.infra.config.db_config import DBConnectionHandler
from app.infra.entities.users_entity import User
from pydantic import EmailStr  # pylint: disable=no-name-in-module


class UserRepository(UserRepositoryInterface):
    """Manages user repository."""

    @classmethod
    def insert_one(cls, name: str, email: EmailStr, password: str) -> UserModel:
        """Insert data into user entity.
        Args:
            name (str): User name.
            email (EmailStr): User email.
            password (str): User password.
        Return:
            Data model of the added user.
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

    @classmethod
    def select_one(
        cls, user_id: Optional[int] = None, user_email: Optional[EmailStr] = None
    ) -> UserModel:
        """Select user by id or email.
        Args:
            user_id (int): User unique identifier.
            user_email (EmailStr): User registred email.
        Return:
            User data model containing specified user.
        """
        try:
            with DBConnectionHandler() as db_connection:
                if user_id is not None:
                    query_result = (
                        db_connection.session.query(User).filter_by(id=user_id).one()
                    )
                elif user_email is not None:
                    query_result = (
                        db_connection.session.query(User)
                        .filter_by(email=user_email)
                        .one()
                    )
                else:
                    raise ValueError
            return UserModel(
                id=query_result.id,
                name=query_result.name,
                email=query_result.email,
                password=query_result.password,
                created_at=query_result.created_at,
            )
        except Exception as exc:
            db_connection.session.rollback()
            raise ConnectionError from exc
        finally:
            db_connection.session.close()
