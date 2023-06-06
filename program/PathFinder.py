from nodes import *
import pandas as pd
import time
import random
import os

program_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(program_directory)

# read the Excel file into a DataFrame
df = pd.read_excel('edges.xlsx')



def find_paths(current, dest, queue, path, paths):
    if current == dest:
        paths.append(path)
        return

    for neighbor in current.connections:
        if neighbor not in path:
            find_paths(neighbor,dest,queue,path + [neighbor], paths)



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



def path_finder():
    prints("Hello there traveler! You look cold and in a hurry. I will try to find you a warm path to your destination.")
    cursor()
    print()
    prints("Firstly, where are you?")
    print()
    n1 = input()
    prints("I see. Where would you like to go?")
    print()
    n2 = input()
    node1 = next(filter(lambda x: x.name == n1.upper(),Nodes))
    node2 = next(filter(lambda x: x.name == n2.upper(),Nodes))
    prints("Okay...")
    cursor()
    prints("Let's see...")
    cursor()
    print()
    print()
    all_paths(node1,node2)


path_finder()
     
