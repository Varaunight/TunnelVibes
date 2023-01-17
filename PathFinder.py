from nodes import *

def find_paths(current, dest, queue, path, paths):
    if current == dest:
        paths.append(path)
        return

    for neighbor in current.connections:
        if neighbor not in path:
            find_paths(neighbor,dest,queue,path + [neighbor], paths)

def all_paths(node1, node2):
    queue = [node1]
    path = [node1]
    paths = []

    find_paths(node1, node2, queue, path, paths)

    return paths

def name_paths(lop):
    namedpaths = []
    for path in lop:
        if isinstance(path, list):
            namedpaths.append(name_paths(path))
            continue

        namedpaths.append(path.name)

    print(namedpaths)


name_paths(all_paths(B1, B2))


