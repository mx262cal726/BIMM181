__author__ = 'rouse'
<<<<<<< HEAD


def recursive_path_finder(i, cycle_list, node_class, current_path, limit):
    split_commas = str(node_class[i].edges)
=======
import random

def recursive_path_finder(loc, cycle_list, node_class, current_path, limit):
    split_commas = str(node_class[loc].edges)
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
    split_commas = split_commas.split(",")
    current_node = int(split_commas[0])
    if limit == len(node_class)*2:
        print "PATH:", current_path
        return cycle_list

<<<<<<< HEAD
    if len(split_commas) > 1:
        for i in range(0, len(split_commas)):
            print "i:", split_commas[i], i
            tmp = get_string(i, split_commas)

            print get_cycle(int(split_commas[i]), node_class, cycle_list)
            node_class[int(split_commas[i])].index = int(split_commas[i])
            node_class[int(split_commas[i])].edges = int(split_commas[i])
            cycle_list[int(split_commas[i])] = get_cycle(int(split_commas[i]), node_class, cycle_list )
            print "cyclelist:", cycle_list[int(split_commas[i])]

            print "index", i, "tmp: ", tmp
            cycle_list[i] = tmp

            recursive_path_finder(int(split_commas[i]),cycle_list, node_class, current_path+","+split_commas[i], limit+1)
=======



    if len(split_commas) > 1:
        for i in range(0, len(split_commas)):
            tmp = get_string(i, split_commas)

           # node_class[loc].index = loc]
            print i, tmp, "TMP",loc
            node_class[loc].edges = tmp
            print "line 19", int(split_commas[i]),get_cycle(int(split_commas[i]),node_class, cycle_list)
            cycle_list[int(split_commas[i])] = str(loc)+","+get_cycle(int(split_commas[i]), node_class, cycle_list )
            print "line 21", int(split_commas[i]),get_cycle(int(split_commas[i]),node_class, cycle_list)



            #recursive_path_finder(int(split_commas[i]),cycle_list, node_class, current_path+","+split_commas[i], limit+1)
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b


    current_path += ","+split_commas[0]
    limit += 1
    return recursive_path_finder(current_node, cycle_list, node_class, current_path, limit)


class Node:
<<<<<<< HEAD
    def __init__(self, index, edges):
        self.index = index
        self.edges = edges
=======
    def __init__(self, index, edges, degree,cycles):
        self.index = index
        self.edges = edges
        self.degree = degree
        self.cycles = cycles

    def Node(self):
        self.edges = list()
        self.cycles = list()

    def make_cycle_list(self):
        self.cycles = list()

    def add_edge(self,edge):
        self.edges.append(edge)

    def add_cycle(self,cycle):
        self.cycles.append(cycle)

>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b


def get_cycle(index, node_list, cycle_list):
    print "cycle_list", cycle_list
<<<<<<< HEAD
=======
    print "nodeList:", node_list[index].index,node_list[index].edges
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
    tmp_list = [None]*len(node_list)
    copy = index
    deep_copy = index
    print deep_copy, "I"
    print "index::",index
    while True:
<<<<<<< HEAD
        next_val = str(node_list[index].edges)
        split = next_val.split(",")
        print "index",index,split
        if tmp_list[index] is None:
            print "index",index,split

            tmp_list[index] = split[0]
            index = int(split[0])
=======

        next_val = node_list[index].edges
        if tmp_list[index] is None:
            print "index",index,next_val

            tmp_list[index] = next_val[0]
            index = int(next_val[0])
            if deep_copy == index:
                break
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
        else:
            break
    path = str(copy)
    next_node = str(copy)
    while True:
        if next_node is not None:
<<<<<<< HEAD

            print "next_node:", next_node,tmp_list[copy]
            if tmp_list[copy] is None:
                break
            next_node = tmp_list[copy]
            print "next again:", next_node
=======
            if tmp_list[copy] == deep_copy:
                break
            if tmp_list[copy] is None:
                break
            next_node = tmp_list[copy]
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
            tmp_list[copy] = None
            copy = int(next_node)
            path += ","+str(copy)
        else:
            break
<<<<<<< HEAD
    print "path:", path, "index", deep_copy

    cycle_list.insert(deep_copy, path)
    print "index", deep_copy, "value", cycle_list[deep_copy]
    print cycle_list
    return path


=======
    print "line 69", "index:", deep_copy, path
    return path


def store_cycles(node_list,index):
    node_list[index].make_cycle_list()
    save = set()
    save.add(index)
    if node_list[index].degree > 1:
        for i in range(0,len(node_list[index].edges)):
            print i, len(node_list[index].edges)
            edge = int(node_list[index].edges[i])
            print edge
            path = str(index)
            if edge == index:
                return
            while edge not in save:
                save.add(edge)
                path += ","+str(edge)
                edge = int(node_list[edge].edges[0])

            node_list[index].add_cycle(path)
            print(path)
        print "cycles", node_list[index].cycles
    return node_list


def count_edges(node_list):
    count = 0
    for i in range(0,len(node_list)):
        edges = node_list[i].edges
        count += len(edges)
    return count


def grab_cycle(index, node_list, doubles, stack, counter):
    stack.append(str(index))


    edges_count = count_edges(node_list)
    print "edge count:", edges_count

    while counter < edges_count:
        node = node_list[index].edges
        degree = node_list[index].degree
        if degree > 1:
            for i in range(0, degree ):
                couple = str(index)+","+str(node[i])
                print "couple;", couple
                if couple not in doubles:
                    print counter,stack
                    counter +=2
                    stack.append(str(node[i]))
                    print stack
                    doubles.add(couple)
                    print "node i ", node[i]
                    grab_cycle(node_list[int(node[i])].index,node_list,doubles,stack,counter)
                else:
                    return stack
        else:
            couple = str(index)+","+str(node[0])
            print "ccccc",couple, doubles
            if couple not in doubles:
                counter +=2
                stack.append(str(node[0]))
                doubles.add(couple)
                print "node I :" ,node[0]
                grab_cycle(node_list[int(node[0])].index,node_list,doubles,stack,counter)
            else:
                return stack






>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
def eulerian_cycle(text):
    in_file = open(text)
    lines = in_file.read().split("\n")
    lines_list = sorted(list(lines))
    eulerian_array  =  [0]*len(lines_list)
    nodes_list = [0]*len(lines_list)
    print eulerian_array
    print lines_list
<<<<<<< HEAD
=======
    i = 0
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
    for line in lines_list:
        line_split = line.split(" ")
        print line_split
        for val in range(0, len(line_split)):
            if line_split[val].isdigit():
<<<<<<< HEAD
                nodes_list[int(line_split[0])] = Node(int(line_split[0]), line_split[2])
                eulerian_array[int(line_split[0])] = line_split[2]
    print "size: ", len(lines)
    print "NODES:", nodes_list[2].index,nodes_list[2].edges
=======
                print line_split[0], line_split[2]
                edges = line_split[2].split(",")
                tmpl = list()

                for e in range(0, len(edges)):
                    tmpl.append(edges[e])

                nodes_list[int(line_split[0])] = Node(int(line_split[0]), tmpl,len(edges),None)
                #print "NODES:", nodes_list[i].edges, nodes_list[i].degree
                eulerian_array[int(line_split[0])] = line_split[2]
                i+=1
    print "size: ", len(lines)
    cycle_list = list()*10*2

    for i in range(0,len(nodes_list)):
        if nodes_list[i].degree > 1:
            print "NODES:", i,nodes_list[i].index,nodes_list[i].edges, nodes_list[i].degree
            nodes_list = store_cycles(nodes_list,i)
    print "c",nodes_list[2].cycles
    tmp = set()
    stack = list()
    size = len(nodes_list)
    index = random.randint(0, size-1)
    best_cycle = grab_cycle(index,nodes_list,tmp,stack,0)
    print best_cycle
    return





>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
    tmp_list = path_list = ["0->"]*len(lines)
    list_index = [0]*len(lines)

    path_count = 0
    path = "0->"
    print len(eulerian_array)
<<<<<<< HEAD

=======
    edges_set = get_cycle_set(eulerian_array)

    copy_set = edges_set
    path_stack = ""
    edge_stack = Stack
    nodes = list(edges_set)
    node_stack = list()
    current_node = nodes[0]
    counter = len(nodes)-1
    node_stack.append(current_node)
    while len(node_stack) < len(nodes):
        edge = get_edge(current_node)
        for i in range(0, len(nodes)):
            print i, nodes
            if nodes[i] != current_node:
                node_index = get_index(nodes[i])
                if edge == node_index and nodes[i] in copy_set and nodes[i] not in node_stack:
                    current_node = nodes[i]

                    node_stack.append(nodes[i])
                    print "nodestack: ", node_stack, nodes[i]
                    edge = get_edge(nodes[i])
                    copy_set.remove(nodes[i])
                    print node_stack
                    #nodes.pop(i)
                    break
            print i , len(nodes)
            print "nodes list:",nodes
            print "set edges:",edges_set
            print "stack:",node_stack
            print i == len(nodes)
            if i >= len(nodes)-1:

                copy_set = set(nodes)
                node_stack = clear(node_stack)
                starting_node = random.randint(0,counter)
                print "Starting Node:", starting_node

                current_node = nodes[starting_node]
                print "current node",current_node
                break


        print "NODE STACK:",node_stack
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
    possible_paths = list()
    possible_paths.insert(0,"0")
    current_path = "0"
    path_count = 0
    count = 0
    current_node = count
    cycle_list = [None]*len(eulerian_array)
<<<<<<< HEAD
    print recursive_path_finder(0, cycle_list, nodes_list, current_path, 0)
=======
    cycle_list  = list(recursive_path_finder(0, cycle_list, nodes_list, current_path, 0))
    print cycle_list
    final_path = ""
    for i in range(0, len(cycle_list)):
        current_cycle = cycle_list[i]
        cycle_list[i] = None
        if current_cycle is not None:
            cycle_split = current_cycle.split(",")
            index_cycle = i

            next_index = i+1
            for next_index in range(next_index,len(cycle_list)):
                next_cycle = cycle_list[next_index]
                #cycle_list[next_index] = None
                if next_cycle is not None:
                    combine_path(current_cycle, next_cycle)
            i = next_index+1
    print final_path


def clear(text):
    while len(text) != 0:
        text.pop()
    return text


class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def clear(self):
         while self.isEmpty() is not True:
             self.pop()
         return self

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def get_edge(node):
    edge = node.split(",")
    return edge[1]


def get_index(node):
    index = node.split(",")
    return index[0]


def get_cycle_set(eulerian_cycle):

    cycle_set =  set()

    for i in range(0, len(eulerian_cycle)):
        edges = eulerian_cycle[i].split(",")
        for j in range(0, len(edges)):
            cycle_set.add(str(i)+","+edges[j])
    print "cycle set",cycle_set
    return cycle_set


def combine_path(path1, path2):
    final_path = list()
    final_path1 = list()
    path1 = path1.split(",")
    path2 = path2.split(",")
    hit = True
    for j in range(0, len(path1)-1):
        if hit:
            for z in range(0, len(path2)-1):
                print path1,"paths", path2
                print path1 + path2
                print path1[j],path2[z],path1[j+1], path2[z+1]
                print path1[0:2]
                if path1[j] == path2[z] and path1[j+1] == path2[z+1]:
                    print path1[0:j],path2[j+1:len(path2)]
                    final_path = path1[0:j+j-1]+path2[z+z-1:len(path2)]
                    final_path1 = path2[0:z]+path1[j:len(path1)]
                    if len(final_path) < len(final_path1):
                        final_path = final_path1

                    hit = False
    print final_path

>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b


def get_string(index, text):
    print "text: ",text,index
    start = 0
    if index == 0:
        tmp = text[1]
        start = 2
    else:
        tmp = text[0]
        start = 1
    for i in range(start, len(text)):
        if i == index:
            continue
        else:
            tmp += ","+text[i]
    return tmp


def get_next_node(path, array, index,max):
    if max == 0:
        return path
    split = array[int(index)].split(",")
    print len(split)
    for x in split:
        if x.isdigit():
            path += x+"->"+array[int(x)]+"->"
            return get_next_node(path,array, array[int(x)],max-1)




<<<<<<< HEAD
eulerian_cycle("rosalind_ba3d.txt")
=======
eulerian_cycle("graphs.txt")
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
