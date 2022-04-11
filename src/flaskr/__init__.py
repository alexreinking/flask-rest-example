from flask import Flask


def create_app():
    """
    Application factory for Flask. Will need to be extended with database support.
    """

    app = Flask(__name__)

    from . import main
    app.register_blueprint(main.bp)

    return app
