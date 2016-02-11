__author__ = 'Kyle Rouse'


def main(text):
    lines = open(text).read().split("\n")

    print pattern_to_number("CGC")


def pattern_to_number(pattern):
    if pattern <= 0:
        return 0
    symbol = last_symbol(pattern)
    prefix = get_prefix(pattern)
    return 4*pattern_to_number(prefix) + symbol_to_number(symbol)


def last_symbol(pattern):
    if len(pattern) == 0:
        return 0
    return pattern[-1]


def get_prefix(symbol):
    if len(symbol) == 0:
        return 0
    return symbol[0:-1]


def symbol_to_number(symbol):
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3
    else:
        return 0


def get_kmers(k):
    kmers = [""]*4**k
    quarter = 4**k
    nucs = ['A', 'C', 'G', 'T']
    for i in range(k):
        quarter /= 4
        for j in range(4**k):
            if quarter == 1:
                index =(j)%4
            elif (j%quarter) == 0:
                index =(j/4)%4
            kmers[j] += (nucs[index])
    print kmers


if __name__ == '__main__':
    print main("input.txt")
