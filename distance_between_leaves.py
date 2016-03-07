__author__ = 'kyle rouse'


def main(text):
    lines = open(text).read().split("\n")
    n = int(lines[0])
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    print distance_between_leaves(n, lines[1:])

def distance_between_leaves(n,data):
    tree = getTree(n, data)


def getTree(n, data):
    tree = Tree()
    isLeaf = True
    for i in range(len(data)):
        if i == n:
            isLeaf = False
        arrow = data[i].split("->")
        dist = arrow[1].split(":")
        tree.addNode(Node(arrow[0],dist[0],dist[1], isLeaf))
    return tree

class Tree(object):
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNode(self, index=0):
        return self.nodes[index]

class Node():
    def __init__(self, index, parent, distance, leaf):
        self.index = index
        self.parent = parent
        self.distance = distance
        self.leaf = leaf

    def isLeaf(self):
        return self.leaf


if __name__ == '__main__':
    main("input")
