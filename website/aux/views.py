from flask import Blueprint, render_template, url_for
from flask_login import current_user

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("home.html")