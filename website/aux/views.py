from flask import Blueprint, render_template, url_for, request, session, redirect
from flask_login import current_user
from aux.program.nodes import nodes
from aux.program.tunnels_cls import Node
from aux.program.PathFinder import *


views = Blueprint("views", __name__)


@views.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        start = request.form["from"]
        end = request.form["to"]
        session['previous_from'] = start
        session['previous_to'] = end

        return redirect(url_for("views.to", start = start, end = end))
    else:
        previous_from = session.get('previous_from')
        previous_to = session.get('previous_to')
        return render_template("home.html", objects = nodes, previous_to = previous_to, previous_from = previous_from)


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/<start>_to_<end>", methods=["GET","POST"])
def to(start, end):
    # output is a list of strings
    output = []

    if request.method == "POST":
        start = request.form["from"]
        end = request.form["to"]
        session['previous_from'] = start
        session['previous_to'] = end

        return redirect(url_for('views.to', start = start, end = end))

    else:
        node1 = next(filter(lambda x: x.name == start.upper(),Nodes))
        node2 = next(filter(lambda x: x.name == end.upper(),Nodes))

        pathlist = paths(node1, node2)

        if len(pathlist) == 0:
                output.append("No paths dawg")

        for path in pathlist:
            output.append(paths_as_strings(path))

        return render_template("to.html", objects = nodes, start = start, end = end, output = output)
    

@views.route("/<start>_to_<end>_<index>")
def path(start, end, index):
    return render_template("path.html", start = start, index = index, end = end)

