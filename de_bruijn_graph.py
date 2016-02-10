__author__ = 'rouse'


def de_bruijn_graph(text):
    kmer_list = list()
    k = 4
    new_k = k-1
    for i in range(0, len(text)-new_k+1):
        kmer_list.insert(i, text[i:i+new_k])
    print overlap_graph_problems(sorted(kmer_list))


def de_bruijn_graph_kmers(text):
    kmer_list = list()
    in_file = open(text)
    lines = in_file.read().split("\n")
    for i in range(0, len(lines)):
        if len(lines[i])> 1:
            kmer_list.insert(i, lines[i])
    print overlap_graph_problems(sorted(kmer_list))


def overlap_graph_problems(kmers):
    suffix_list = lex_order_suffix(kmers)
    prefix_list = lex_order_prefix(kmers)
    prefix_set =  sorted(set(prefix_list))
    directed_list = list()
    index = 0
    tracker = 0
    copy = ""
    for prefix in prefix_set:
        first_kmer = True
        count = 0
        for i in range(0, len(suffix_list)):
            if get_suffix(prefix) == get_prefix(get_prefix(suffix_list[i])) and prefix[0] == suffix_list[i][-1]:
                if first_kmer is True:
                    copy = get_prefix(suffix_list[i])
                    directed_list.insert(index, prefix+"->"+copy)
                    first_kmer = False
                    count += 1
                    index += 1
                else:
                    copy += ","+suffix_list[i]
                    directed_list[index-1] += ","+get_prefix(suffix_list[i])
                    count += 1
            tracker += 1
        tracker = count

    ordered_list = sorted(directed_list)
    for i in range(0, len(ordered_list)):
        print ordered_list[i]



def list_to_set(list_in):
    set_out = set()
    for item in list_in:
        set_out.add(item)
    return set_out


def fix_kmer(kmer):
    kmer = kmer[-1] + kmer[0: len(kmer)-1]
    return kmer


def get_prefix(kmer):
    if len(kmer) <= 1:
        return ""
    else:
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

def lex_order_prefix(kmers):
    kmer_list = list(kmers)
    for i in range(0, len(kmers)):
        kmer_list[i] = get_prefix(kmers[i])
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

de_bruijn_graph_kmers("input")
