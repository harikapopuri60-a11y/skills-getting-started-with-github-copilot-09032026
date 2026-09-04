from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    email = "new.student@mergington.edu"
    activity_name = "Chess Club"

    post_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert post_response.status_code == 200

    delete_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert delete_response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]
