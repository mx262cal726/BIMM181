__author__ = 'kyle rouse'

dict = {'A': None,'C':None,'G':None,'T':None,'Z':None}

def trie_construction(genome, patterns):
    print Trie(patterns)

    trie = [(0,genome[0])]
    nodes = [Node(0, genome[0],[None]*5) ]
    tree = Trie(nodes)
    for i in range(1, len(genome)):
        trie.append((i,genome[i]))
        node = Node(i,genome[i],[None]*5)
        node.add_edge(to_number(genome[i]),len(tree.nodes))
        tree.add_node(node)
    for pattern in patterns:
        currNode = tree.nodes[0]
        for i in range(1,len(pattern)+1):
            sym = pattern[i-1]
            if currNode.value == sym:
                currNode = tree.nodes[i]
            elif currNode.edges[to_number(sym)] is not None:
                currNode = tree.nodes[currNode.edges[to_number(sym)]]

            else:
                print "currentNode:",currNode.edges[to_number(sym)],currNode.index,sym
                new_node = Node(len(tree.nodes),sym, [None]*4)
                new_node.add_edge(to_number(sym),len(tree.nodes)+1)
                tree.add_node(new_node)


    for i in range(1,len(tree.nodes)+1):
        print str(tree.nodes[i-1].index)+"->"+str(i)+":"+tree.nodes[i-1].value


def to_number( value):

    if value == 'A':
        return 0
    elif value == 'C':
        return 1
    elif value == 'G':
        return 2
    elif value == 'T':
        return 3
    return 4


class Trie(object):

    def __init__(self, pattern):
        self.nodes = [Node(0, 0, [], False)]*2
        self.edges = {}


        if type(pattern) is str:
            self.add_node(pattern)
        else:
            for word in pattern:
                self.add_node(word)

    def new_node(self):
        node = Node(0, 0, [], False)
        self.nodes.append(node)
        return node

    def add_pattern(self, pattern):
        current = 1
        for child in self.nodes[current].child:
            if self.edges[current, child] == pattern[0]:
                return self.add_pattern(pattern[1:], child)
        return current, pattern


    def add_node(self, pattern):
        node, tex = self.add_pattern(pattern)
        for i in range(0, len(node)):
            index = len(self.nodes) + 1
            self.nodes[index] = self.new_node(node, self.nodes[node].d + 1)
            self.nodes[tex].child.append(index)
            self.edges[node, index] = tex[i]
            node = index
        self.nodes[node].end = True


    def print_nodes(self):
        for i in self.nodes:
            for j in i.edges:
                i.print_edges()

    def last_element(self):
        return len(self.nodes)-1


class Node:
    def __init__(self, parent, d, child, leaf):
        self.d = d
        self.parent = parent
        self.child = child
        self.leaf = leaf

    def add_edge(self,value, index):
        print "Value::",value,index
        print self.edges[value]
        if self.edges[value] is None:
            self.edges[value] = index
            print self.edges[value],"here"
            return

    def is_assigned(self,value):
        print "VALUE:", value,self.edges[value]
        return self.edges[value]
        if self.edges[value] is not None:
            return 1
        return 0

    def get_edges(self, nuc):
        print self.edges[nuc]
        if self.edges[nuc] is not None:
            return self.edges[nuc]
        else:
            return self.size - 1

    def print_edges(self):
        for i in range(0,len(self.edges)):
            print "index",i, self.edges[i]



def main(text):
    lines = open(text).read().split("\n")
    genome = lines[0]
    patterns = lines[1:]
    print patterns
    print trie_construction(genome, patterns)


if __name__ == '__main__':
    main("input")
