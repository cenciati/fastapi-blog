from os import getenv
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

load_dotenv(find_dotenv())
DB_USER: Optional[str] = getenv("DB_USER")
DB_PASSWORD: Optional[str] = getenv("DB_PASSWORD")
DB_HOST: Optional[str] = getenv("DB_HOST")
DB_NAME: Optional[str] = getenv("DB_NAME")


class DBConnectionHandler:
    """SQLAlchemy database connection helper."""

    def __init__(self) -> None:
        self.__connection_string: str = (
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
        )
        self.sesion = None

    def get_engine(self) -> Engine:
        """Creates a connection engine using a database
        connection string.

        Return:
            Connection engine.
        """

        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(  # pylint: disable=attribute-defined-outside-init
            autocommit=False, autoflush=False, bind=engine
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # type: ignore
