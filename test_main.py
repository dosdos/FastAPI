from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_roll_dice():
    response = client.get("/roll-dice")
    assert response.status_code == 200
    json_response = response.json()
    assert isinstance(json_response, dict)
    assert 'num' in json_response
    assert isinstance(json_response['num'], int)
    assert 1 <= json_response['num'] <= 6
