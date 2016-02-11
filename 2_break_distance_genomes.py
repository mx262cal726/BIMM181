__author__ = 'Kyle'


def two_break_distance_genomes(p, q):
    model = map(int, list(p.strip("()").split(" ")))
    genomes = list()
    sub_gene = q.split(")(")
    for i in range(0, len(sub_gene)):
        genome = sub_gene[i].strip("()").split(" ")
        genome_list = list()
        for j in genome:
            genome_list.append(j)
        print "Genomes:",genome_list
        genomes.append(map(int,genome_list))
        print genomes
    for i in range(1, len(model)):
        try:
            for j in range(0, len(genomes)):
                for x in range(0, len(genomes[j])):
                    if i != genomes[j][x]:
                        tmp = list()
                        tmp = greedy_sorting_reversals(genomes[j])
                        print tmp
                    elif j > 0:
                        combine = list()
                        combine = fusion(sub_gene, genomes, i)
                        print "Combine:", combine
                    else:
                        raise stop
        except stop:
            pass

class stop(Exception): pass


def fusion(sub_gene, genomes, i):
    tmp = list(genomes[0])
    print tmp, i, tmp[0]
    for j in range(1, len(genomes)):
        current = genomes[j]
        if i == abs(current[0]):
            t = list(tmp[i-1:])+current
            print "T:",t
            return t


def reversal(p, index):
    queue = list()
    for i in range(index, len(p)+1):
        if index != abs(int(p[i-1])):
            queue.append(int(p[i-1])*-1)
        else:
            queue.append(int(p[i-1])*-1)
            tmp = list()
            f = map(lambda x: tmp.append(int(x)), queue)
            return tmp
    return p


def add_signs(copy):
    signs = list()
    for i in copy:
        if i < 0:
            signs.append(i)
        else:
            signs.append("+"+str(i))
    return signs

def greedy_sorting_reversals(text):
    dist = 0
    seq_list = text
    container = list()
    for i in range(1, len(seq_list)+1):
        if i != seq_list[i-1]:

            tmp = reversal(seq_list,int(i))

            tmp.reverse()
            copy = list(seq_list)
            if i > 1:
                copy = seq_list[0:i-1]+tmp+seq_list[i-1+len(tmp):len(seq_list)]
            else:
                copy = tmp +seq_list[len(tmp):len(seq_list)]

            container.append(add_signs(copy))

            x = int(copy[i-1])
            if x < 0:
                tmp = list(copy)
                tmp.remove(x)
                seq_list = list(tmp)
                seq_list.insert(i-1, int("+"+str(abs(x))))
                container.append(add_signs(seq_list))
            else:
                seq_list = list(copy)
                dist += 1

    return container


if __name__ == '__main__':
    lines = open("input").read().split("\n")
    print two_break_distance_genomes(lines[0],lines[1])

