__author__ = 'rouse'


def recursive_path_finder(i, cycle_list, node_class, current_path, limit):
    split_commas = str(node_class[i].edges)
    split_commas = split_commas.split(",")
    current_node = int(split_commas[0])
    if limit == len(node_class)*2:
        print "PATH:", current_path
        return cycle_list

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


    current_path += ","+split_commas[0]
    limit += 1
    return recursive_path_finder(current_node, cycle_list, node_class, current_path, limit)


class Node:
    def __init__(self, index, edges):
        self.index = index
        self.edges = edges


def get_cycle(index, node_list, cycle_list):
    print "cycle_list", cycle_list
    tmp_list = [None]*len(node_list)
    copy = index
    deep_copy = index
    print deep_copy, "I"
    print "index::",index
    while True:
        next_val = str(node_list[index].edges)
        split = next_val.split(",")
        print "index",index,split
        if tmp_list[index] is None:
            print "index",index,split

            tmp_list[index] = split[0]
            index = int(split[0])
        else:
            break
    path = str(copy)
    next_node = str(copy)
    while True:
        if next_node is not None:

            print "next_node:", next_node,tmp_list[copy]
            if tmp_list[copy] is None:
                break
            next_node = tmp_list[copy]
            print "next again:", next_node
            tmp_list[copy] = None
            copy = int(next_node)
            path += ","+str(copy)
        else:
            break
    print "path:", path, "index", deep_copy

    cycle_list.insert(deep_copy, path)
    print "index", deep_copy, "value", cycle_list[deep_copy]
    print cycle_list
    return path


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
                nodes_list[int(line_split[0])] = Node(int(line_split[0]), line_split[2])
                eulerian_array[int(line_split[0])] = line_split[2]
    print "size: ", len(lines)
    print "NODES:", nodes_list[2].index,nodes_list[2].edges
    tmp_list = path_list = ["0->"]*len(lines)
    list_index = [0]*len(lines)

    path_count = 0
    path = "0->"
    print len(eulerian_array)

    possible_paths = list()
    possible_paths.insert(0,"0")
    current_path = "0"
    path_count = 0
    count = 0
    current_node = count
    cycle_list = [None]*len(eulerian_array)
    print recursive_path_finder(0, cycle_list, nodes_list, current_path, 0)


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




eulerian_cycle("rosalind_ba3d.txt")