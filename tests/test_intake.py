"""Form tests through Flask (Member A: Aarav)."""

import pytest

from app import create_app


@pytest.fixture()
def client():
    return create_app({"TESTING": True}).test_client()


def test_form_page_loads(client):
    page = client.get("/new")
    assert page.status_code == 200
    assert b"New repair request" in page.data


def test_valid_request_is_accepted(client):
    form = {"rider_label": "Rider 12", "bike_type": "city", "problem": "Flat rear tire"}
    page = client.post("/new", data=form)
    assert page.status_code == 200
    assert b"Request is valid" in page.data


def test_invalid_request_shows_errors_and_saves_nothing(client):
    form = {"rider_label": "", "bike_type": "mountain", "problem": "   "}
    page = client.post("/new", data=form)
    assert page.status_code == 400
    assert b"Nothing was saved" in page.data
    assert b"Choose city, road or other." in page.data


def test_preferred_day_is_never_shown_as_confirmed(client):
    form = {
        "rider_label": "Rider 3",
        "bike_type": "road",
        "problem": "Brakes squeak",
        "preferred_day": "Saturday",
    }
    page = client.post("/new", data=form)
    assert b"not a booking" in page.data
    assert b"confirmed" not in page.data.lower()