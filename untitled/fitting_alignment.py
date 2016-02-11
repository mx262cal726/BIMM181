__author__ = 'kyle'


def get_score(s1, s2):
    if s1 == s2:
        return 1
    else:
        return -1


def fitting_alignment(seq_one, seq_two):

    matrix = [[0 for _ in range(len(seq_two)+1)] for _ in range(len(seq_one)+1)]
    backtrack = [[0]*(len(seq_two)+1) for _ in range(len(seq_one)+1)]

    for i in range(1, len(seq_one)+1):
        for j in range(1, len(seq_two)+1):
            scores = [matrix[i-1][j] - 1, matrix[i][j-1] - 1, matrix[i-1][j-1] + get_score(seq_one[i-1], seq_two[j-1])]
            matrix[i][j] = max(scores)
            backtrack[i][j] = scores.index(matrix[i][j])

    for i in matrix:
        print i
    high = 0
    for i in range(1, len(matrix)):
        if matrix[i][len(matrix[i])-1] >= high:
            x, y = i, len(matrix[i])-1
            high = matrix[i][len(matrix[i])-1]
    one_aligned, two_aligned = seq_one[:x], seq_two[:y]
    indel = lambda word, i: word[:i] + '-' + word[i:]
    while x*y != 0:
        if backtrack[x][y] == 0:
            x -= 1
            two_aligned = indel(two_aligned, y)
        elif backtrack[x][y] == 1:
            y -= 1
            one_aligned = indel(one_aligned, x)
        elif backtrack[x][y] == 2:
            x -= 1
            y -= 1
    one_aligned = one_aligned[x:]
    return high, one_aligned, two_aligned


def fitting_alignment_setup(text):
    in_file = open(text)
    lines = in_file.read().split("\n")

    seq_one = lines[0]
    seq_two = lines[1]

    score, seq1, seq2 = fitting_alignment(seq_one, seq_two)
    tmp = str(score)+"\n"+seq1+"\n"+seq2
    return tmp

print fitting_alignment_setup("input.txt")

