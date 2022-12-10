from app.domain.models.post_model import PostModel


def test_post_dto(post_model_example: PostModel) -> None:
    # Assert
    assert post_model_example is not None
    assert isinstance(post_model_example, PostModel)
    assert post_model_example.dict() == {
        "id": post_model_example.id,
        "title": post_model_example.title,
        "content": post_model_example.content,
        "published": post_model_example.published,
        "created_at": post_model_example.created_at,
        "updated_at": post_model_example.updated_at,
    }
