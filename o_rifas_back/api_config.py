import os

from flask import Flask

def config_app(
    app: Flask = None,
) -> None:
    """
    Configure a Flask app instance.

    :param app: The Flask app instance to configure.
    """

    app.config['API_TITLE'] = 'O rIFAS REST API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'