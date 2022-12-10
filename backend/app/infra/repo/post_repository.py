from typing import Optional

from app.domain.models.post_model import PostModel
from app.infra.config.db_config import DBConnectionHandler
from app.infra.entities.posts_entity import Post


class PostRepository:
    """Manages post repository."""

    @classmethod
    def insert_one(
        cls, title: str, content: str, published: Optional[bool] = True
    ) -> PostModel:
        """Insert data into post entity.
        Args:
            title (str): Post title.
            content (str): Post body/content.
            published (bool): Whether the post should be published immediately.
        Return:
            Data model of the added post.
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_post = Post(title=title, content=content, published=published)
                db_connection.session.add(new_post)
                db_connection.session.commit()
                return PostModel(title=title, content=content, published=published)
            except Exception as exc:
                db_connection.session.rollback()
                raise ConnectionError from exc
            finally:
                db_connection.session.close()

    @classmethod
    def select_one(
        cls, post_id: Optional[int] = None, post_title: Optional[str] = None
    ) -> PostModel:
        """Select post by id or title.
        Args:
            post_id (int): Post unique identifier.
            post_title (str): Post title.
        Return:
            Post data model containing specified post.
        """
        try:
            with DBConnectionHandler() as db_connection:
                if post_id is not None:
                    query_result = (
                        db_connection.session.query(Post).filter_by(id=post_id).one()
                    )
                elif post_title is not None:
                    query_result = (
                        db_connection.session.query(Post)
                        .filter_by(title=post_title)
                        .one()
                    )
                else:
                    raise ValueError
            return PostModel(
                id=query_result.id,
                title=query_result.title,
                content=query_result.content,
                published=query_result.published,
                created_at=query_result.created_at,
                updated_at=query_result.updated_at,
            )
        except Exception as exc:
            db_connection.session.rollback()
            raise ConnectionError from exc
        finally:
            db_connection.session.close()
