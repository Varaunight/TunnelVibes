from aux.program.nodes import *
import pandas as pd
import time
import random
import os

# read the Excel file into a DataFrame
df = pd.read_excel('aux/program/edges.xlsx')



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


x=10
def prints(text):
    if x == 1:
        for char in text:
            print(char, end='',flush=True)
            time.sleep(random.uniform(0,0.1))
    else:
        print(text)

def cursor():
    time.sleep(0.3)

    

def all_paths(node1, node2):
    queue = [node1]
    path = [node1]
    paths = []

    find_paths(node1, node2, queue, path, paths)

    namedpaths = []
    for path in paths:
        namedpaths.append(nodename(path))

    if len(namedpaths) == 0:
        prints("It seems that there are no completely internal paths from " + node1.name + " to " + node2.name + ". Brace for the weather traveler.")
        return
    else: 
        prints("The possible paths from "+node1.name+" to "+node2.name+" are: ")
        print()
        for path in namedpaths:
            prints(str(namedpaths.index(path) + 1) + "." + str(path))
            print()
            cursor()

    prints("Choose your preferred path by selecting a number from 1 to " + str(len(namedpaths)) + ", or press 'q' to exit: ")
    choice = input()
    if choice.upper() == 'Q':
        prints("Have a nice day!")
        return
    else:
        prints("Okay!")
        print()
        time.sleep(1)
        prints("*ehem*")
        print()
        time.sleep(1)
        prints("Here we go!")
        print()
        time.sleep(1)
        prints("...drumroll please...")
        print()
        print()
        time.sleep(1)

        prints("Starting at "+node1.name+": ")
        print()
        directions = make_dir(paths[(int(choice) - 1)])
        i = 0
        cur_path = namedpaths[(int(choice)-1)]
        for dir in directions:
            prints(str(directions.index(dir) + 1)+ ": ["+ cur_path[i] +"] ---> " + dir + ". ---> ["+cur_path[i+1]+"]")
            i+=1
            cursor()
            print()
        prints("You've arrived at "+cur_path[-1]+"! Big ups! Enjoy your wadeva. Laters :D")



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
         
