# Tunnel classes

class Graph:
    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes


class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_edge(new, node):
        node.edges.append(new)

    def printcons(self):
        print([node.name for node in self.connections])



def is_connected(node1, node2):
    return node1 in node2.connections

class Edge:
    def __init__(self, node1, node2, value=0):
        self.node1 = node1
        self.node2 = node2
        self.value = value
        node1.connections.append(node2)
        node2.connections.append(node1)