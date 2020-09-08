__version__ = '0.1.0'

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    with app.app_context():
        from . import routes

        return app
