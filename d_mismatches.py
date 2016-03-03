__author__ = 'kyle rouse'

import suffix_array

def inverse_burrows_wheeler(text):
    text,matrix = get_matrix(text)
    itext = lambda x: x[1:]+x[0]
    text = itext(text)
    return text


def last(text):
    return text[-1]


def first_occurrence(gene, text):
    for i in range(len(gene)):
        if gene[i] == text:
            return i


def last_occurrence(gene,text):
    last = len(gene)-1
    for i in range(len(gene)):
        if gene[last - i] == text:
            return last - i


def last_to_first( matrix,last):
        return matrix[last][1][2]


def get_matrix(text):
    text_order = [i for i in text]
    text_order.sort()
    order_tup = []
    for i in range(0,len(text)):
        order_tup.append((text[i],i))
    order_tup.sort()
    matrix = [[(i,0) for i in range(0,2)] for _ in range(0,len(text))]

    for i in range(0,len(matrix)):
        matrix[i][-1] = (text[i],i)
        matrix[i][0] = (order_tup[i])
    index = 0
    answer = ""
    j = 0
    for i in range(0, len(matrix)+1):
        if i != len(matrix):
            answer += matrix[index][0][0]
        index = matrix[index][0][1]
        matrix[index][1] = (matrix[index][1][0],matrix[index][1][1],j)
        j = index

    return answer,matrix


def get_count_n(dict,count,sym,gene,matrix):
    for i in range(0,len(matrix)):
        if sym == matrix[i][1][0]:
            return matrix[i][1][2]
#            return count[i][dict[sym]]


def get_count_bottom(dict,count,sym,gene,matrix):
    for i in range(0,len(matrix)):
        if sym == matrix[-i-1][1][0]:
            return matrix[-i][1][2]
#            return count[i][dict[sym]]


def bw_matching(gene, matrix, patterns,d):
    answer = [0]*len(patterns)
    answers = [0]*len(patterns)
    print len(patterns)
    for index in range(0, len(patterns)):
        print index
        top = last_to_first(matrix,first_occurrence(gene,patterns[index][-1]))
        bottom = last_to_first(matrix, last_occurrence(gene,patterns[index][-1]))
        next_bottom = bottom
        bottom_sym = matrix[bottom][0][0]
        next_top = top
        top_sym =  matrix[top][0][0]
        end_top = True
        end_bottom = True
        while top < bottom:

            noequal_top = True
            noequal_bottom = True
            tmp = ""
            d_top = 0
            d_bottom = 0
            for i in range(1,len(patterns[index])+1):

                if noequal_bottom and end_bottom:
                    tmp +=bottom_sym
                    if bottom_sym == patterns[index][-i]:
                        if i == len(patterns[index]):
                            print next_bottom
                            answers[index] += 1
                            #end_bottom = False
                    else:
                        if d_bottom >= d:
                            noequal_bottom = False
                        else:
                            d_bottom += 1

                if noequal_top and end_top:
                    if top_sym == patterns[index][-i]:
                        if i == len(patterns[index]):
                            print next_top

                            answers[index] += 1
                            #end_top = False
                    else:
                        if d_top >= d:
                            noequal_top = False
                        else:
                            d_top += 1
                next_bottom = matrix[next_bottom][1][2]
                bottom_sym = matrix[next_bottom][0][0]
                next_top = matrix[next_top][1][2]
                top_sym = matrix[next_top][0][0]

            if end_top:
                top += 1
            if end_bottom:
                bottom -= 1
            if end_top is False and end_bottom is False:
                break

            top_sym = matrix[top][0][0]
            bottom_sym = matrix[bottom][0][0]
            next_top = top
            next_bottom = bottom
        answer[index] = abs(bottom-top)

    return answers


def count_n(bw):
    var = set(i for i in bw)
    count = {var.pop():i for i in range(len(var))}
    count_matrix = [[0 for _ in range(len(count))] for _ in range(1)]

    for i in range(1,len(bw)+1):
        tmp = list(count_matrix[i-1])
        tmp[count[bw[i-1]]] += 1
        count_matrix.append(tmp)
    return count,count_matrix


def test(ans,my):

    if ans == my:
        print "PASS", len(ans),len(my)
    else:
        print "FAILED",len(ans),len(my)

def get_btw(text):
    itext = lambda x: text[-1]+text[:-1]
    m = []
    for i in range(0, len(text)):
        m.append(text)
        text = itext(text)
    m.sort()
    return m


def main(text):
    lines = open(text).read().split("\n")
    gene = lines[0]
    bw = get_btw(gene)
    bw_seq = ""
    for i in bw:
        bw_seq += i[-1]
    print bw_seq
    text, matrix = get_matrix(bw_seq)

    for i in matrix:
        print i
    bw = get_btw(gene)
    bw_seq = ""
    suffixArray = suffix_array.suffix_array(gene)

    answer = bw_matching(bw_seq, matrix, lines[1].split(" "),int(lines[2]))
    for i in answer:
        print i,
    answer = bw_matching(bw_seq, matrix, lines[1:])
    ans = []
    for i in answer:
        ans.append(suffixArray[i])
    ans.sort()
    for i in ans:
        print i,
if __name__ == '__main__':
    main("input")
