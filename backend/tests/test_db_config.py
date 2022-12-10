from app.infra.config.db_config import (
    DB_HOST,
    DB_NAME,
    DB_PASSWORD,
    DB_USER,
    DBConnectionHandler,
)
from sqlalchemy.engine import Engine

db_connection = DBConnectionHandler()


def test_when_create_an_engine_return_engine_object():
    # Arrange
    engine = db_connection.get_engine()

    # Act/Assert
    assert isinstance(engine, Engine)


def test_connection_string_text():
    # Arrange
    engine: Engine = db_connection.get_engine()

    # Act
    actual_connection_string: str = str(engine.url)
    expected_connection_string: str = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )

    # Assert
    assert actual_connection_string == expected_connection_string
