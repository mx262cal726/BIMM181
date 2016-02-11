
def greedy_sorting_reversals(text):
    dist = 0
    seq_list = map(int,list(text.strip("()").split(" ")))
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

def add_signs(copy):
    signs = list()
    for i in copy:
        if i < 0:
            signs.append(i)
        else:
            signs.append("+"+str(i))
    return signs

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

def main():
    in_file = open("rosalind_ba6a.txt")
    lines = in_file.read().split("\n")
    seq = lines[0]
    for i in greedy_sorting_reversals(seq):
        line = "("+str(i[0])
        for j in range(1, len(i)):
            line += " "+str(i[j])
        line += ")"
        print line

if __name__ == '__main__':
    main()
