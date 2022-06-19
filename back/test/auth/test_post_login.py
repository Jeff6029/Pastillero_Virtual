from src.lib.utils import temp_file

from src.webserver import create_app

from src.domain.user import UserRepository, User


def setup():
    user_repository = UserRepository(temp_file())
    app = create_app(repositories={"users": user_repository})
    client = app.test_client()

    jeff = User(id_user="user-j", name="Jefferson", password="user-j")
    user_repository.save(jeff)

    return client


def test_should_validate_login():
    client = setup()

    body = {"id_user": "user-j", "password": "user-j"}
    response_post = client.post("/auth/login", json=body)
    assert response_post.status_code == 200

    response = response_post.json
    assert response["id_user"] == "user-j"
    assert response["name"] == "Jefferson"


def test_should_return_error_for_wrong_password():
    client = setup()

    body = {"id_user": "user-j", "password": "nanana"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 401


def test_should_fail_if_user_not_exists():
    client = setup()

    body = {"id_user": "user-Laura", "password": "laura"}
    response = client.post("/auth/login", json=body)

    assert response.status_code == 401
