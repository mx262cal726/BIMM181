__author__ = 'rouse'


def overlap_graph_problem(kmers):
    kmers_list = order_kmers_lex(kmers)
    suffix_sorted = lex_order_suffix(kmers_list)
    directed_list = [[], []]
    listss = list()
    count = 0
    track = 0
    prev_suffix = ""
    for i in range(0, len(suffix_sorted)):
        if len(suffix_sorted[i]) <= 1:
            continue
        current_suffix = suffix_sorted[i]
        if current_suffix[0:-1] == prev_suffix[0:-1]:
            count += 1
            continue
        while count < len(kmers_list):
            if current_suffix[0:-1] == kmers_list[count][0:-1]:
                listss.insert(count, fix_kmer(current_suffix)+" -> "+kmers_list[count])
                count += 1
                track += 1
            else:
                count += 1
                continue
        count = track
    listss = sorted(listss)
    for i in range(0, len(listss)):
        print listss[i]


def fix_kmer(kmer):
    kmer = kmer[-1] + kmer[0: len(kmer)-1]
    return kmer


def get_prefix(kmer):
    return kmer[0: len(kmer)-1]


def get_suffix(kmer):
    return kmer[1: len(kmer)]


def lex_order_suffix(kmers):
    kmer_list = list(kmers)
    for i in range(0, len(kmers)):
        if len(kmers[i]) <= 1:
            continue
        kmer_list[i] = kmers[i][1: len(kmers[i])] + kmers[i][0]
    return sorted(kmer_list)


def order_kmers_lex(kmers):
    file_in = open(kmers)
    lines = file_in.read().split("\n")
    return sorted(lines)


def composition_of_string(k, text):
    kmer_list = list()
    for i in range(0, len(text)-k+1):
        kmer_list.append(text[i:i+k])
    sorted_list = sorted(kmer_list)
    for i in sorted_list:
        print i

overlap_graph_problem("rosalind_ba3e.txt")