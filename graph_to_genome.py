__author__ = 'kyle rouse'


def cycle_to_chromosome(cycle):
    print cycle
    nodes = [None]*((len(cycle))/2)
    for i in range(1, (len(cycle)/2)+1):
        if cycle[2*i-2] < cycle[2*i-1]:
            nodes[i-1] = "+"+str(cycle[(2*i-1)]/2)
        else:
            nodes[i-1] = str(-(cycle[2*i-1]/2)-1)
    print nodes
    return nodes

def graph_to_genome(node):
    P = set()
    for i in node:
        print "Node:", node
        chrome = cycle_to_chromosome(i)
        print "chrome:",chrome
        P.add(str(chrome))
    print "P:",P
    z = [None]*len(P)
    while len(P) > 0:
        tmp = P.pop()
        print "tmp:",tmp
        for j in range(0, len(tmp)):
            if tmp[j].isdigit():
                print "for:", tmp[j]
                if tmp[j-1] == '+':
                    z[int(tmp[j])-1] = "-"+tmp[j:j+1]
                else:
                    z[int(tmp[j])-1] = "+"+tmp[j:j+1]

    print z
    return z

def main(text):

    lines = open(text).readline().lstrip('(').rstrip(')').split("), (")
    l = [None]*len(lines)
    for i in range(0,len(lines)):
        hold = map(int,lines[i].split(", "))
        l[i] = (hold)
    k = graph_to_genome(l)
    front = k[:len(k)/2]
    print front
    print "("+" ".join(graph_to_genome(l))+")"








if __name__ == '__main__':
    main("input")
