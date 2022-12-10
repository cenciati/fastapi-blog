from app.domain.models.user_model import UserModel


def test_user_dto(user_model_example: UserModel):
    # Assert
    assert user_model_example is not None
    assert isinstance(user_model_example, UserModel)
    assert user_model_example.dict() == {
        "id": user_model_example.id,
        "name": user_model_example.name,
        "email": user_model_example.email,
        "password": user_model_example.password,
        "created_at": user_model_example.created_at,
    }
