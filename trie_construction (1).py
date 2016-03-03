__author__ = 'Kyle Rouse'


def trie_construction(gene, patterns):

    trie = Trie(Node(0, {'A':None,'C':None,'G':None,'T':None}, None, (gene[0],0)))
    for i in range(1,len(gene)):
        trie.nodes.append(Node(0,{'A':None,'C':None,'G':None,'T':None},None,(gene[i],i)))
    first_list = []
    ans = ""
    out = open("output2", 'w')

    for pattern in patterns:
        current = pattern
        gene_node = trie.nodes[0]
        size = len(trie.nodes)
        for i in range(0, len(pattern)):

            if gene_node.value[0] == pattern[i] and size != len(trie.nodes):
                gene_node = trie.nodes[gene_node.value[1]+1]

            elif gene_node.child[pattern[i]] is not None:
                size = len(trie.nodes)
                val = gene_node.child[pattern[i]].value[1]-1
                gene_node = trie.nodes[val]

            else:

                if gene_node.end is not True:
                    gene_node.end = False

                node = Node(gene_node,{'A':None,'C':None,'G':None,'T':None}, None,(pattern[i],len(trie.nodes)+1))
                if gene_node.check_assigned(pattern[i]):
                    gene_node.child[pattern[i]] = node
                if i >= len(pattern)-1 and gene_node.end is not True:
                    node.end = True
                elif gene_node.end is not True:
                    node.end = False
                trie.nodes.append(node)
                gene_node = node
                size = len(trie.nodes)
            if i == 0:
                first_node = gene_node
        print size, len(trie.nodes)

        if size == len(trie.nodes):
            out.write(str(first_node.value[1])+" ")
            first_list.append(first_node.value[1])

    return trie.answer()



class Trie(object):
    def __init__(self, root):
        self.root = root
        self.nodes = [root]

    def answer(self):
        count = 0
        out = open("ouput", 'w')
        answer = []
        out.write(str(count)+"->"+str(count+1)+":"+self.nodes[0].value[0])
        for i in self.nodes:
            if i.parent is 0:
                ans = str(count)+"->"+str(count+1)+":"+i.value[0]
            else:
                p = i.parent
                ans = str(i.parent.value[1])+"->"+str(i.value[1])+":"+str(i.value[0])
            answer.append(ans)
            if count > 0:
                out.write("\n"+ans)
            count += 1
        return answer

    def get_last(self):
        return self.nodes[len(self.nodes)-1]

    def add_child(self, index, letter, node):
        if index > 5:
            index -= 2
        self.nodes[index].child[letter] = node

    def print_tree(self):
        for i in self.nodes:
            if i.parent == 0:
                parent = 'No Parent:'
            else:
                parent = i.parent.value[1]
            print "Parent:",parent,"Value:",i.value[0],i.value[1],i.end


class Node(object):
    def __init__(self, parent, child, end, value):
        self.parent = parent
        self.child = child
        self.end = end
        self.value = value

    def check_assigned(self, val):
        if self.child[val] is None:
            return True
        return False

    def info(self):
        if self.parent == 0:
            parent = 'No Parent:'
        else:
            parent = self.parent.value[1]
        c = ""
        for i in self.child:
            if i is not None:
                c += i
        print "Parent:",parent,"Value",self.value[0],self.value[1],"Child:",c


def main(text):
    lines = open(text).read().split("\n")
    t = Trie(lines)
    alines = open("answer").read().split("\n")

    answer = set(alines)

    ans = trie_construction(lines[0],lines[1:])
    ans.sort()
    sorted(answer)
    for i in ans:
        print i,
    print "pass"

if __name__ == '__main__':
    main("input")