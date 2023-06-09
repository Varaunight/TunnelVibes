from flask import Blueprint, render_template, url_for, request, session
from flask_login import current_user
from aux.program.nodes import nodes
from aux.program.tunnels_cls import Node
from aux.program.PathFinder import *



views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    # output is a list of strings
    output = []

    if request.method == "POST":
        start = request.form["from"]
        end = request.form["to"]
        session['previous_from'] = start
        session['previous_to'] = end
        node1 = next(filter(lambda x: x.name == start.upper(),Nodes))
        node2 = next(filter(lambda x: x.name == end.upper(),Nodes))
        pathlist = paths(node1, node2)


        if len(pathlist) == 0:
            output.append("No paths dawg")

        for path in pathlist:
            output.append(paths_as_strings(path))
        

        return render_template("home.html", objects = nodes, start = start, end = end, print = pathlist, output = output)
    else:
        previous_from = session.get('previous_from')
        previous_to = session.get('previous_to')
        return render_template("home.html", objects = nodes, previous_to = previous_to, previous_from = previous_from, output = output)

@views.route("/about")
def about():
    return render_template("about.html")


