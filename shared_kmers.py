__author__ = 'kyle rouse'

from collections import defaultdict
from string import maketrans


def rev(dna):
    comp = maketrans('ATCG', 'TAGC')
    return dna.translate(comp)[::-1]


def shared_kmers(k, dna1, dna2):
    dna1_dict = defaultdict(list)
    for i in range(len(dna1)-k+1):
        dna1_dict[dna1[i:i+k]].append(i)

    return {(i,j) for j in range(len(dna2)-k+1) for i in dna1_dict[dna2[j:j+k]] + dna1_dict[rev(dna2[j:j+k])]}

def main(text):
    lines = open(text).read().split("\n")
    answer = map(str, shared_kmers(int(lines[0]),lines[1],lines[2]))
    print '\n'.join(answer)

if __name__ == '__main__':
    main("rosalind_ba6e.txt")
