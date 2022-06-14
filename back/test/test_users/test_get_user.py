from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.user import UserRepository, User


def test_should_return_empty_list_user():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    response = client.get("/api/users")

    assert response.json == []


def test_should_return_list_of_users():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    jeff = User(
        id_user="user-1",
        name="Jefferson",
    )
    johan = User(
        id_user="user-2",
        name="Johan",
    )

    user_repository.save(jeff)
    user_repository.save(johan)

    response = client.get("/api/users")
    assert response.status_code == 200

    response_users = response.json
    assert len(response_users) == 2

    assert response_users[0]["id_user"] == "user-1"
    assert response_users[0]["name"] == "Jefferson"
    assert response_users[1]["id_user"] == "user-2"
    assert response_users[1]["name"] == "Johan"
