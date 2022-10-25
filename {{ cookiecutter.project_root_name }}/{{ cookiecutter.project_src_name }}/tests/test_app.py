from esmerald.testclient import EsmeraldTestClient

from ..main import get_application


def create_app():
    app = get_application()
    return app


def get_client():
    return EsmeraldTestClient(create_app())


def test_welcome_endpoint():
    client = get_client()

    response = client.get("/api/v1/welcome")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to your application"}


def test_welcome_api_view():
    client = get_client()

    response = client.get("/api/v1/welcome-apiview/world")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to your application using APIView"}


def test_deny_access_api():
    client = get_client()

    response = client.get("/api/v1/welcome-apiview/world/deny")

    assert response.status_code == 403
