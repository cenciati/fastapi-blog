from app.domain.models.post_model import PostModel
from app.infra.entities.posts_entity import Post
from app.infra.repo.post_repository import PostRepository
from faker import Faker
from sqlalchemy.engine import Engine


def test_insert_one_new_post(
    faker: Faker,
    post_repository: PostRepository,
    engine: Engine,
) -> None:
    # Arrange
    title: str = faker.pystr()
    content: str = faker.text()

    # Act
    new_post: PostModel = post_repository.insert_one(title=title, content=content)
    query_post: Post = engine.execute(  # type: ignore
        f"SELECT * FROM posts WHERE title = '{new_post.title}'"
    ).fetchone()

    # Teardown
    engine.execute(f"DELETE FROM posts WHERE title = '{new_post.title}'")

    # Assert
    assert query_post is not None
    assert new_post.title == query_post.title
    assert new_post.content == query_post.content


def test_select_one_post(
    faker: Faker,
    post_repository: PostRepository,
    engine: Engine,
) -> None:
    # Arrange
    title: str = faker.pystr()
    content: str = faker.text()

    # Act
    engine.execute(
        f"INSERT INTO posts (title, content) VALUES ('{title}', '{content}')"
    )
    query_post: PostModel = post_repository.select_one(post_title=title)

    # Teardown
    engine.execute(f"DELETE FROM posts WHERE title = '{title}'")

    # Assert
    assert query_post is not None
    assert query_post.title == title
    assert query_post.content == content
