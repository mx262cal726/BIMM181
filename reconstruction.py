__author__ = 'kyle'


def reconstruction(text):
    in_file = open(text)
    lines = in_file.read()
    split_lines = lines.split("\n")
    order_list = sorted(list(split_lines[1:len(split_lines)]))
    tmp = list(sorted(order_list))
    k = int(split_lines[0])

    suff_list = suffix_first(k,tmp)
    print suff_list
    print "order list ", order_list
    reconstructed =""
    tmp = list()
    order_list = list(order_list)
    list_size = len(order_list)

    for i in range(0,len(order_list)):
        suffix = back(k,order_list[i])
        print(suffix)
        front_kmer = order_list[i]
        print "size: ",list_size
        for j in range(0,len(order_list)):
            print j, list_size, order_list
            back_kmer = order_list[j]

            if i != j:
                prefix = front(k,back_kmer)
                print suffix, " == ",prefix
                if suffix == prefix and suffix != "" and prefix != "":
                    if reconstructed == "":
                        reconstructed = front_kmer+back(k,back_kmer)
                        tmp.append(front_kmer)
                        tmp.append(back_kmer)
                        order_list[i] = ""
                        order_list[j] = ""
                        suffix = back(k,back_kmer)
                        break
                        print tmp, order_list
                    else:
                        tmp.append(back_kmer)
                        order_list[j] = ""
                        reconstructed += back(k,back_kmer)

            print reconstructed
        print reconstructed
        print tmp


def front(k,text):
    return text[0:k/2]


def back(k,text):
    return text[k/2:k]


def suffix_first(k,text):
    for i in range(0, k):
        text[i] = back(k,text[i])+front(k,text[i])
    return sorted(text)


reconstruction("input.txt")