"""My validation tests (Member A: Aarav). I chose these inputs and expected results."""

import pytest

from app.validation import validate_request

VALID = {
    "rider_label": "Rider 12",
    "bike_type": "city",
    "problem": "Flat rear tire",
    "preferred_day": "",
}


def test_valid_request_has_no_errors():
    clean, errors = validate_request(VALID)
    assert not errors
    assert clean["problem"] == "Flat rear tire"


def test_spaces_are_trimmed():
    clean, errors = validate_request({**VALID, "rider_label": "  Rider 12  "})
    assert not errors
    assert clean["rider_label"] == "Rider 12"


@pytest.mark.parametrize(
    "field,value",
    [
        ("rider_label", ""),  # missing rider label
        ("rider_label", "x" * 31),  # rider label too long
        ("bike_type", ""),  # no bike type
        ("bike_type", "mountain"),  # unsupported bike type
        ("problem", ""),  # blank problem
        ("problem", "    "),  # only spaces counts as blank
        ("problem", "x" * 241),  # problem too long
        ("preferred_day", "x" * 41),  # preferred day too long
    ],
)
def test_invalid_input_is_rejected(field, value):
    _, errors = validate_request({**VALID, field: value})
    assert field in errors


@pytest.mark.parametrize(
    "field,value",
    [
        ("problem", "x" * 240),  # exactly the limit is allowed
        ("preferred_day", "x" * 40),
        ("bike_type", "road"),
        ("bike_type", "other"),
    ],
)
def test_edge_values_are_allowed(field, value):
    _, errors = validate_request({**VALID, field: value})
    assert not errors
