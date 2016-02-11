__author__ = 'Kyle Rouse'

def motif_enumeration(k, d, dna):

    patterns = set()
    return

def main(text):
    lines = open(text).read().split("\n")
    line0 = lines[0].split(" ")
    k = line0[0]
    d = line0[1]
    tmp = list(lines[1:len(lines)])
    print tmp,k,d
    return motif_enumeration(k, d, tmp)

if __name__ == '__main__':
    print main("input.txt")