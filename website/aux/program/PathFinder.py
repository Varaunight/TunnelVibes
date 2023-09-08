from aux.program.nodes import *
import pandas as pd
import time
import random
import os

# Def took this dataframe code from the internet 
df = pd.read_excel('aux/program/edges.xlsx')


# Depth first search for finding my paths
def find_paths(current, dest, queue, path, paths):
    if current == dest:
        paths.append(path)
        return

    for neighbor in current.connections:
        if neighbor not in path:
            find_paths(neighbor,dest,queue,path + [neighbor], paths)


# Takes a list of nodes and returns a new list, with their names instead
def nodename(lon):
    nodes = []
    for node in lon:
        nodes.append(node.name)

    return nodes


# Takes a list of nodes and returns a list of the directions to get there
def make_dir(lon):
    directions = []
    i = 0
    while len(lon) > 1:
        # search for the pair of entries
        search_pair = (lon[0].name, lon[1].name)
        matching_rows = df[(df['First'] == search_pair[0]) & (df['Second'] == search_pair[1])]

        # print the entry from the next row
        try:
            directions.append(matching_rows['Route A'].iloc[0])
        except Exception:
            search_pair = (lon[1].name, lon[0].name)
            matching_rows = df[(df['First'] == search_pair[0]) & (df['Second'] == search_pair[1])]
            directions.append(matching_rows['Route B'].iloc[0])

        lon.pop(0)

    return directions
    

# Takes two nodes and returns a list (of lists) all the paths between these nodes,
# and then calls nodename on all the nodes in the paths
def paths(node1, node2):
    queue = [node1]
    path = [node1]
    paths = []

    find_paths(node1, node2, queue, path, paths)

    namedpaths = []
    for path in paths:
        namedpaths.append(nodename(path))

    return namedpaths


# Takes a list of nodes and returns their names connected with arrows
def paths_as_strings(lon):
    string_path = "hello"
    if len(lon) == 0:
        string_path = "There seems to be no internal pathways to your destination. Sorry about that."
    else:
        check = 0
        for node in lon:
            if check == 0:
                string_path = node
                check +=1
            else:
                string_path = string_path + " --> " + node

    return string_path
         