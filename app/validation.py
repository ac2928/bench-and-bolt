"""Rules for a new repair request (Member A: Aarav). No Flask, no database."""

BIKE_TYPES = ("city", "road", "other")
RIDER_LABEL_MAX = 30
PROBLEM_MAX = 240
PREFERRED_DAY_MAX = 40


def validate_request(form):
    """Check a submitted form. Return (clean_values, errors).

    If errors is not empty, nothing should be saved.
    """
    rider_label = (form.get("rider_label") or "").strip()
    bike_type = (form.get("bike_type") or "").strip()
    problem = (form.get("problem") or "").strip()
    preferred_day = (form.get("preferred_day") or "").strip()

    errors = {}
    if not rider_label:
        errors["rider_label"] = "Enter a rider label, like Rider 12."
    elif len(rider_label) > RIDER_LABEL_MAX:
        errors["rider_label"] = (
            f"Keep the rider label to {RIDER_LABEL_MAX} characters or fewer."
        )

    if bike_type not in BIKE_TYPES:
        errors["bike_type"] = "Choose city, road or other."

    if not problem:
        errors["problem"] = "Describe the problem."
    elif len(problem) > PROBLEM_MAX:
        errors["problem"] = f"Keep the problem to {PROBLEM_MAX} characters or fewer."

    if len(preferred_day) > PREFERRED_DAY_MAX:
        errors["preferred_day"] = (
            f"Keep the preferred day to {PREFERRED_DAY_MAX} characters or fewer."
        )

    clean = {
        "rider_label": rider_label,
        "bike_type": bike_type,
        "problem": problem,
        "preferred_day": preferred_day,
    }
    return clean, errors