__author__ = 'kyle rouse'


def trie_matching(text, gene):
    count = 0
    answers = []
    print text, gene
    for pattern in text:
        current = pattern[0]
        print current
        i = 0
        stop = len(gene)
        while i < stop:
            if current != gene[i]:
                current = pattern[0]
                i = i - count
                count = 0
            else:
                print pattern
                print current, count, "==",len(pattern)-1
                if count == 0:
                    start = i
                if count == len(pattern)-1:
                    i = i - count
                    count = 0
                    current = pattern[0]
                    print "start",start
                    answers.append(gene[start:start+len(pattern)-1])
                else:
                    count += 1
                    current = pattern[count]
            i += 1
    answers.sort()
    for i in answers:
        print i
    print answers
    return answers



def build_trie(gene):
    trie = Trie(Node(0, {'A':None,'C':None,'G':None,'T':None,'$':None}, None, (gene[0],0),0))
    for i in range(1,len(gene)):
        trie.nodes.append(Node(0,{'A':None,'C':None,'G':None,'T':None,'$':None},None,(gene[i],i),0))
    return trie

def trie_construction(gene, patterns):

    trie = build_trie(gene)
    first_list = []
    ans = ""
    out = open("output2", 'w')
    new_gene = ""
    prev = ""
    suffix = []
    for pattern in patterns:
        current = pattern
        gene_node = trie.nodes[0]
        size =0
        count = 0
        first = True
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
                tmp = abs(int(gene_node.value[1]) - len(trie.nodes))
                if tmp > 1:
                    print pattern, len(pattern)
                    if len(pattern)-i <= 2:
                        suffix.append(pattern)
                    else:
                        print "i:",i,pattern[i],pattern[i+1:]
                        suffix.append(pattern[i])
                        suffix.append(pattern[i+1:])
                node = Node(gene_node,{'A':None,'C':None,'G':None,'T':None,'$':None}, None,(pattern[i],len(trie.nodes)+1),0)

                if gene_node.check_assigned(pattern[i]):
                    gene_node.child[pattern[i]] = node

                if i >= len(pattern)-1 and gene_node.end is not True:
                    node.end = True


                elif gene_node.end is not True:
                    node.end = False
                if first:
                    first = False
                    first_no = node

                trie.nodes.append(node)
                new_gene += str(node.value[0])
                gene_node = node
                size = len(trie.nodes)
            if i == 0:
                first_node = gene_node

        print size, len(trie.nodes)

        if size == len(trie.nodes):
            out.write(str(first_node.value[1])+" ")
            first_list.append(first_node.value[1])

    trie.answer()
    for i in suffix:
        print i
    print "end"
    return trie


def test(ans, alines):
    for i in range(0, len(alines)):
        if alines[i] != ans[i]:
            print "Fail at:",i, alines[i], "!=", ans[i]
            return
        elif i == len(alines)-1:
            print "pass test"
            return


def get_suffix_list(text):
    suffix = []
    for i in range(1,len(text)):
        suffix.append(text[i:])
    return suffix


def main(text):
    lines = open(text).read().split("\n")
    suffix = get_suffix_list(lines[0])
    print suffix, lines[0]
    t = ""
    ans = trie_construction(lines[0], suffix)
    for i in ans.nodes:
        t += i.value[0]
    print t

    alines = map(int,list(open("answer").read().split(" ")))
    corrent_ans = map(int,alines)

    corrent_ans.sort()



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
    def __init__(self, parent, child, end, value,repeat):
        self.parent = parent
        self.child = child
        self.end = end
        self.value = value
        self.repeat = repeat

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
if __name__ == '__main__':
    main("input")


