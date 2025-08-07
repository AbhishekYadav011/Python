from fastapi.testclient import TestClient
from carsharing import app
from unittest.mock import Mock
from schema import Car, CarInput, User
from routers.cars import add_car

client = TestClient(app)

def test_add_car():
    response = client.post("/api/cars", 
                           json={"doors": 4, "size": "xxl"},headers={"Authorization": "Bearer Abhi011"}, cookies={"cars_cookie": ""})
    assert response.status_code == 200
    car = response.json()
    assert car["doors"] == 4
    assert car["size"] == "xxl"


"""Mocking the session to test add_car function
 without hitting the database or performing actual I/O operations."""
def test_add_car_with_mock_session():
    mock_session = Mock()
    input = CarInput(doors=7, size="xxl")
    user = User(username="Abhi011")
    result = add_car(mock_session, user, input)

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()
    assert isinstance(result, Car)
    assert result.doors == 7
    assert result.size == "xxl"