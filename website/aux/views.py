from flask import Blueprint, render_template, url_for, request
from flask_login import current_user
from ...program.nodes import *


views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        start = request.form["from"]
        end = request.form["to"]
        return render_template("home.html", start = start, end = end, objects = objects)
    else:
        return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html")

