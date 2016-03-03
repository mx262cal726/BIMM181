__author__ = 'kyle rouse'


def cycle_to_chromosome(cycle):
    nodes = [None]*((len(cycle))/2)
    for i in range(1, (len(cycle)/2)+1):
        if cycle[2*i-2] < cycle[2*i-1]:
            nodes[i-1] = "+"+str(cycle[(2*i-1)]/2)
        else:
            nodes[i-1] = str(-(cycle[2*i-1]/2)-1)
    return nodes


def main(text):
    lines = open(text).read().split("\n")
    cycle = map(int,lines[0].strip("()").split(" "))
    answer = " ".join(map(str,cycle_to_chromosome(cycle)))
    answer = "("+answer+")"
    print answer


if __name__ == '__main__':
    main("rosalind_ba6g.txt")
