__author__ = 'kyle'


def local_alignment_score(seq_one, seq_two, scoring_matrix, penalty):

    matrix = [[0 for _ in range(len(seq_two)+1)] for _ in range(len(seq_one)+1)]
    backtrack = [[0]*(len(seq_two)+1) for _ in range(len(seq_one)+1)]

    for i in range(1, len(seq_one)+1):
        for j in range(1, len(seq_two)+1):
            scores = [matrix[i-1][j] - penalty, matrix[i][j-1] - penalty,
                      matrix[i-1][j-1] + scoring_matrix[seq_one[i-1], seq_two[j-1]], 0]
            matrix[i][j] = max(scores)
            backtrack[i][j] = scores.index(matrix[i][j])
    indel = lambda word, i: word[:i] + '-' + word[i:]

    for i in matrix:
        print i
    high = 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if int(matrix[i][j]) > high:
                high = int(matrix[i][j])
                x, y = i, j


    one_aligned, two_aligned = seq_one[:x], seq_two[:y]
    while backtrack[x][y] != 3 and x*y != 0:
        if backtrack[x][y] == 0:
            x -= 1
            two_aligned = indel(two_aligned, y)
        elif backtrack[x][y] == 1:
            y -= 1
            one_aligned = indel(one_aligned, x)
        elif backtrack[x][y] == 2:
            x -= 1
            y -= 1

    one_aligned, two_aligned = one_aligned[x:], two_aligned[y:]

    return high, one_aligned, two_aligned


class Pam250(object):

    def __init__(self, text):
        scoring_matrix = open(text)
        pairs = [line.strip().split() for line in scoring_matrix.readlines()]
        self.scoring_matrix = {(pair[0], pair[1]):int(pair[2]) for pair in pairs}

    def __getitem__(self, pair):
        return self.scoring_matrix[pair[0], pair[1]]


def local_alignment_setup(text):
    in_file = open(text)
    lines = in_file.read().split("\n")

    seq_one = lines[0]
    seq_two = lines[1]

    score, seq1, seq2 = local_alignment_score(seq_one, seq_two, Pam250("Pam250"), 5)
    tmp = str(score)+"\n"+seq1+"\n"+seq2
    return tmp

print local_alignment_setup("input.txt")

