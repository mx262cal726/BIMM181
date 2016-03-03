__author__ = 'kyle rouse'


def inverse_burrows_wheeler(text):
    text,matrix = get_matrix(text)
    itext = lambda x: x[1:]+x[0]
    text = itext(text)
    return text


def last(text):
    return text[-1]


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

def get_btw(text):
    itext = lambda x: text[-1]+text[:-1]
    m = []
    for i in range(0, len(text)):
        m.append(text)
        text = itext(text)
    m.sort()
    return m


def test(ans,my):

    if ans == my:
        print "PASS", len(ans),len(my)
    else:
        print "FAILED",len(ans),len(my)


def main(text):
    lines = open(text).read().split("\n")
    text, matrix = get_matrix(lines[0])
    print matrix[int(lines[1])][1][2]


if __name__ == '__main__':
    main("rosalind_ba9k.txt")
