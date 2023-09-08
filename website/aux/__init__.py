from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="/static")
    app.config['SECRET_KEY'] = 'hellohello'

    from .views import views
    app.register_blueprint(views, url_prefix="/")


    return app