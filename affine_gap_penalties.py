__author__ = 'kyle'


def global_alignment_score(seq_one, seq_two, scoring_matrix, penalty):

    matrix = [[0 for _ in range(len(seq_two)+1)] for _ in range(len(seq_one)+1) for _ in range(3)]
    backtrack = [[0]*(len(seq_two)+1) for _ in range(len(seq_one)+1) for _ in range(3)]
    for i in matrix:
        for j in matrix[i]:
            print(j)

    for i in range(1, len(seq_one)+1):
        matrix[i][0] = -i*penalty

    for i in range(1, len(seq_two)+1):
        matrix[0][i] = -i*penalty

    for i in range(1, len(seq_one)+1):
        for j in range(1, len(seq_two)+1):
            scores = [matrix[i-1][j] - penalty, matrix[i][j-1] - penalty, matrix[i-1][j-1] + scoring_matrix[seq_one[i-1], seq_two[j-1]]]
            matrix[i][j] = max(scores)
            backtrack[i][j] = scores.index(matrix[i][j])
    indel = lambda word, i: word[:i] + '-' + word[i:]

    one_aligned, two_aligned = seq_one, seq_two

    i, j = len(seq_one), len(seq_two)
    max_score = str(matrix[i][j])

    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            two_aligned = indel(two_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            one_aligned = indel(one_aligned, i)
        else:
            i -= 1
            j -= 1

    for _ in range(i):
        two_aligned = indel(two_aligned, 0)
    for _ in range(j):
        one_aligned = indel(one_aligned, 0)
    return max_score, one_aligned, two_aligned


class Blosum62(object):

    def __init__(self, text):
        scoring_matrix = open(text)
        pairs = [line.strip().split() for line in scoring_matrix.readlines()]
        self.scoring_matrix = {(pair[0], pair[1]):int(pair[2]) for pair in pairs}

    def __getitem__(self, pair):
        return self.scoring_matrix[pair[0], pair[1]]


def global_alignment_setup(text):
    in_file = open(text)
    lines = in_file.read().split("\n")

    seq_one = lines[0]
    seq_two = lines[1]

    score, seq1, seq2 = global_alignment_score(seq_one, seq_two, Blosum62("Blosum62"), 5)
    tmp = str(score)+"\n"+seq1+"\n"+seq2
    return tmp

print global_alignment_setup("input.txt")

