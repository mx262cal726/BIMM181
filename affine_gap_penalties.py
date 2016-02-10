__author__ = 'kyle'


def affine_gap_penalties(seq_one, seq_two, scoring_matrix, penalty, gap_penalty):

    matrix = [[[0 for _ in range(len(seq_two)+1)] for _ in range(len(seq_one)+1)] for _ in range(3)]
    backtrack = [[[0 for _ in range(len(seq_two)+1)] for _ in range(len(seq_one)+1)] for _ in range(3)]

    for i in range(1, len(seq_one)+1):
        matrix[0][i][0] = -penalty-(i-1)*gap_penalty
        matrix[1][i][0] = -penalty-(i-1)*gap_penalty
        matrix[2][i][0] = -10*gap_penalty

    for i in range(1, len(seq_two)+1):
        matrix[2][0][i] = -penalty-(i-1)*gap_penalty
        matrix[1][0][i] = -penalty-(i-1)*gap_penalty
        matrix[0][0][1] = -10*gap_penalty

    for i in range(1, len(seq_one)+1):
        for j in range(1, len(seq_two)+1):
            scores = [matrix[0][i-1][j] - gap_penalty, matrix[1][i-1][j] - penalty]
            matrix[0][i][j] = max(scores)
            backtrack[0][i][j] = scores.index(matrix[0][i][j])
            scores = [matrix[2][i][j-1] - gap_penalty, matrix[1][i][j-1] - penalty]
            matrix[2][i][j] = max(scores)
            backtrack[2][i][j] = scores.index(matrix[2][i][j])
            scores = [matrix[0][i][j], matrix[1][i-1][j-1] +
                      scoring_matrix[seq_one[i-1],seq_two[j-1]], matrix[2][i][j]]
            matrix[1][i][j] = max(scores)
            backtrack[1][i][j] = scores.index(matrix[1][i][j])

    indel = lambda word, i: word[:i] + '-' + word[i:]

    one_aligned, two_aligned = seq_one, seq_two

    i, j = len(seq_one), len(seq_two)
    max_scores = matrix[0][i][j], matrix[1][i][j], matrix[2][i][j]
    max_score = max(max_scores)
    backtrack_score = max_scores.index(max_score)
    while i*j != 0:
        if backtrack_score == 0:
            if backtrack[0][i][j] == 1:
                backtrack_score = 1
            i -= 1
            two_aligned = indel(two_aligned, j)

        elif backtrack_score == 1:
            if backtrack[1][i][j] == 0:
                backtrack_score = 0
            elif backtrack[1][i][j] == 2:
                backtrack_score = 2
            else:
                j -= 1
                i -= 1

        else:
            if backtrack[2][i][j] == 1:
                backtrack_score = 1
            one_aligned = indel(one_aligned, i)
            j -= 1

    for _ in range(i):
        two_aligned = indel(two_aligned, 0)
    for _ in range(j):
        one_aligned = indel(one_aligned, 0)
    return str(max_score), one_aligned, two_aligned


class Blosum62(object):

    def __init__(self, text):
        scoring_matrix = open(text)
        pairs = [line.strip().split() for line in scoring_matrix.readlines()]
        self.scoring_matrix = {(pair[0], pair[1]):int(pair[2]) for pair in pairs}

    def __getitem__(self, pair):
        return self.scoring_matrix[pair[0], pair[1]]


def affine_gap_setup(text):
    in_file = open(text)
    lines = in_file.read().split("\n")

    seq_one = lines[0]
    seq_two = lines[1]

    score, seq1, seq2 = affine_gap_penalties(seq_one, seq_two, Blosum62("Blosum62"), 11, 1)
    tmp = str(score)+"\n"+seq1+"\n"+seq2
    return tmp

print affine_gap_setup("rosalind_ba5j.txt")

