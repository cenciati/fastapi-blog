from os import getenv
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

load_dotenv(find_dotenv())
DB_DRIVER: Optional[str] = getenv("DB_DRIVER")
DB_USER: Optional[str] = getenv("DB_USER")
DB_PASSWORD: Optional[str] = getenv("DB_PASSWORD")
DB_HOST: Optional[str] = getenv("DB_HOST")
DB_PORT: Optional[str] = getenv("DB_PORT")
DB_NAME: Optional[str] = getenv("DB_NAME")


class DBConnectionHandler:
    """SQLAlchemy database connection helper."""

    def __init__(self) -> None:
        self.__connection_string: str = (
            f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        self.__engine = self.__create_database_engine()
        self.sesion = None

    def __create_database_engine(self) -> Engine:
        """Creates a connection engine using a database
        connection string.
        Return:
            Connection engine.
        """
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self) -> Engine:
        """Get connection engine.
        Return:
            Connection engine.
        """
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(  # pylint: disable=attribute-defined-outside-init
            autocommit=False, autoflush=False, bind=self.__engine
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # type: ignore
