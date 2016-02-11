__author__ = 'rouse'


def genomepath_to_string(text):
    file_in = open(text)
    lines = file_in.read().split("\n")
    prev = string_constructed = lines[0]
    for line in lines:
        if get_suffix(prev) == get_prefix(line):
            string_constructed += get_next_nucleotide(line)
        prev = line
    print string_constructed


def get_prefix(kmer):
    return kmer[0: len(kmer)-1]


def get_suffix(kmer):
    return kmer[1: len(kmer)]


def get_next_nucleotide(kmer):
    return kmer[-1]


genomepath_to_string("rosalind_ba3b (4).txt")