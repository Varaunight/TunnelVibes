from flask import Blueprint, render_template, url_for, request, session
from flask_login import current_user
from aux.program.nodes import objects
from aux.program.tunnels_cls import Node
from aux.program.PathFinder import *

nodes = []
for object in objects:
    if isinstance(object, Node):
        nodes.append(object)


views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        start = request.form["from"]
        end = request.form["to"]
        session['previous_from'] = start
        session['previous_to'] = end
        node1 = next(filter(lambda x: x.name == start.upper(),Nodes))
        node2 = next(filter(lambda x: x.name == end.upper(),Nodes))
        pathlist = paths(node1, node2)

        return render_template("home.html", objects = nodes, start = start, end = end, print = pathlist)
    else:
        previous_from = session.get('previous_from')
        previous_to = session.get('previous_to')
        return render_template("home.html", objects = nodes, previous_to = previous_to, previous_from = previous_from)

@views.route("/about")
def about():
    return render_template("about.html")


