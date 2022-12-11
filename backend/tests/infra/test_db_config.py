from app.infra.config.db_config import (
    DB_DRIVER,
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_PASSWORD,
    DB_USER,
)
from sqlalchemy.engine import Engine


def test_if_when_engine_is_created_it_returns_a_sql_alchemy_engine_object(
    engine: Engine,
):
    # Assert
    assert isinstance(engine, Engine)


def test_database_connection_string_text_information(engine: Engine):
    # Arrange
    actual_connection_string = engine.url
    expected_connection_string: list = [
        DB_DRIVER,
        DB_USER,
        DB_PASSWORD,
        DB_HOST,
        DB_PORT,
        DB_NAME,
    ]
    expected_full_connection_string: str = (
        f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Assert
    assert actual_connection_string is not None
    assert actual_connection_string[0] == expected_connection_string[0]
    assert actual_connection_string[1] == expected_connection_string[1]
    assert actual_connection_string[2] == expected_connection_string[2]
    assert actual_connection_string[3] == expected_connection_string[3]
    assert str(actual_connection_string[4]) == expected_connection_string[4]
    assert actual_connection_string[5] == expected_connection_string[5]
    assert str(actual_connection_string) == expected_full_connection_string
