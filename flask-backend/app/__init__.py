from flask import Flask
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from flaskext.markdown import Markdown
from config import BaseConfig

from app.views import main

def create_app(config = BaseConfig):
    app = Flask(__name__)
    Bootstrap(app)
    Markdown(app)
    
    cors = CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config.from_object(config)

    app.register_blueprint(main)

    return app
