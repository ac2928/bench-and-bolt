"""Intake form route (Member A: Aarav)."""

from flask import Blueprint, render_template, request

from .validation import BIKE_TYPES, validate_request

bp = Blueprint("intake", __name__)


@bp.route("/new", methods=["GET", "POST"])
def new_request():
    if request.method == "GET":
        return render_template("new.html", values={}, errors={}, bike_types=BIKE_TYPES)
    values, errors = validate_request(request.form)
    if errors:
        return (
            render_template(
                "new.html", values=values, errors=errors, bike_types=BIKE_TYPES
            ),
            400,
        )
    # Saving and the queue are Member B's part (db.py, queue page).
    return render_template("checked.html", values=values)
