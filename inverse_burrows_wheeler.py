__author__ = 'kyle rouse'


def inverse_burrows_wheeler(text):
    matrix = get_matrix(text)
    itext = lambda x: x[1:]+x[0]
    matrix = itext(matrix)
    return matrix


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
    for i in matrix:
        print i
    for i in range(0,len(matrix)):
        matrix[i][-1] = (text[i],i)
        matrix[i][0] = (order_tup[i])
    index = matrix[0][0][1]
    answer = matrix[0][0][0]
    for i in range(1, len(matrix)):
        answer += matrix[index][0][0]
        index = matrix[index][0][1]
    return answer


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
    ans = open("answer").read().split("\n")

    my = inverse_burrows_wheeler(lines[0])
    return test(ans[0], my)
if __name__ == '__main__':
    main("input")
