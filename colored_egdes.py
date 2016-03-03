__author__ = 'kyle rouse'


def cycle_to_chromosome(cycle):
    nodes = [None]*((len(cycle))/2)
    for i in range(1, (len(cycle)/2)+1):
        if cycle[2*i-2] < cycle[2*i-1]:
            nodes[i-1] = "+"+str(cycle[(2*i-1)]/2)
        else:
            nodes[i-1] = str(-(cycle[2*i-1]/2)-1)
    return nodes


def colored_edges(dna):
    edges = set()
    for i in dna:
        node = cycle_to_chromosome(i)
        for j in range(1,len(i)+1):
            edges.add("("+str(node[2*j-3])+", "+str(node[2*j-2])+")")

    return edges
def main(text):

    lines = open(text).readline().split("\n")
    lines[0].strip("+")
    dna = lines[0].strip("+").lstrip('(').rstrip(')').split(")(")
    genome = list()
    for i in dna:
        genome.append(map(int,i.split(" ")))


    print ", ".join(colored_edges(genome))



if __name__ == '__main__':
    main("rosalind_ba6h.txt")
