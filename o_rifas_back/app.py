from api_config import (
    config_app
)
from controllers.table import (
    blp
)

from flask import Flask
from flask_smorest import Api
from flask_cors import CORS


__version__: str = '0.1.0'

def create_app() -> Flask:
    """
    Create a Flask app instance.

    :return: A Flask app instance.
    """


    app = Flask(__name__)
    config_app(app)
    api = Api(app)

    api.register_blueprint(blp)

    CORS(app)

    return app
