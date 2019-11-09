import os
from flask import Flask
from .api import bp as checkifbestseller
from .product_extractor import ExtractProducts
import configparser


def create_app():
    # initialize flask application
    app = Flask(__name__)

    # register application config from the config file.
    config = configparser.RawConfigParser()
    config.read('config/application.cfg')

    app.config['PORT'] = config.get("main", "PORT")
    app.config['HOST_NAME'] = config.get("main", "HOST_NAME")
    app.config['DEBUG'] = config.get("main", "DEBUG")
    app.config['DB_NAME'] = config.get("main", "DB_NAME")

    # register all blueprints
    app.register_blueprint(checkifbestseller)

    return app
