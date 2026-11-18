"""Bench & Bolt repair queue: Flask app factory."""

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)
    from . import intake

    app.register_blueprint(intake.bp)
    return app
