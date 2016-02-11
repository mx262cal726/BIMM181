__author__ = 'Kyle Rouse'
import random

def gibbs_sampler(dna, k, t, N):
    end = len(dna[0])-k+1
    kmers = get_random_kmers(dna,k)
    best_kmers = list(kmers)
    for i in range(1,N):
        j = random.randint(0,t)
        profile = get_profile_matrix(kmers, j)

    print kmers


def get_profile_matrix(kmers, j):
    nucs = 'ACGT'
    n_list = [0]*len(kmers[0])
    rand_list = [n_list]*4
    for i in range(0, len(kmers[0])):
        for z in range(0, 4):

            for nuc in range(0, len(kmers)):
                print "length:",len(kmers),i,nuc,z
                if(kmers[i][z] == nucs[z]):
                    rand_list[i][z] += 1

    return rand_list


def get_random_kmers(dna, k):
    rand_list = list()
    end = len(dna[0])-k+1
    for i in range(0, len(dna)):
        x = random.randint(0, end)
        rand_list.append(dna[i][x:x+k])
    return rand_list

def main(text):
    lines = open(text).read().split("\n")
    line = lines[0].split(" ")
    dna = list(lines[1:len(lines)])
    k = int(line[0])
    t = int(line[1])
    N = int(line[2])
    print gibbs_sampler(dna, k, t, N)
    print lines


if __name__ == '__main__':
    print main("input.txt")