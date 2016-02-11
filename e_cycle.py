__author__ = 'kyle'

class Node:
    def __init__(self, index, edges):
        self.index = index
        self.edges = edges

    def Node(self):
        self.edges = list()

    def add_edge(self,edge):
        self.edges.append(edge)

def eulerian_cycle(text):
    in_file = open(text)
    lines = in_file.read().split("\n")
    lines_list = sorted(list(lines))
    eulerian_array  =  [0]*len(lines_list)
    nodes_list = [0]*len(lines_list)
    print eulerian_array
    print lines_list
    for line in lines_list:
        line_split = line.split(" ")
        print line_split
        for val in range(0, len(line_split)):
            if line_split[val].isdigit():
                print line_split[0], line_split[2]
                nodes_list[int(line_split[0])] = Node(int(line_split[0]), line_split[2])
                eulerian_array[int(line_split[0])] = line_split[2]
    print "size: ", len(lines)
    print "NODES:", nodes_list[2].index,nodes_list[2].edges
    print nodes_list[2].index
    print final_path

eulerian_cycle("graphs.txt")