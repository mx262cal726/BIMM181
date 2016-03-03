__author__ = 'kyle rouse'


def chromosome_to_cycle(dna):
    nodes = [None]*2*len(dna)
    for i in range(1, len(dna)+1):
        t_dna = int(dna[i-1])
        if t_dna > 0:
            nodes[2*i-2] = 2*t_dna - 1
            nodes[2*i-1] = 2*t_dna
        else:
            nodes[2*i-2] = -2*t_dna
            nodes[2*i-1] = -2*t_dna - 1
    return nodes


def main(text):
    in_data = open(text).readline()
    dna = in_data.strip().lstrip('(').rstrip(')').split(" ")
    answer = " ".join(map(str,chromosome_to_cycle(dna)))
    answer = "("+answer+")"
    print answer

if __name__ == '__main__':
    main("rosalind_ba6f.txt")
