from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_products():

    response = client.get(
        "/api/v1/products/"
    )

    assert response.status_code == 200