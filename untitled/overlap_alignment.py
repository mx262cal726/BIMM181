__author__ = 'kyle'


def get_score(s1, s2):
    if s1 == s2:
        return 1
    else:
        return -2


def overlap_alignment(seq_one, seq_two):

    matrix = [[0 for _ in range(len(seq_two)+1)] for _ in range(len(seq_one)+1)]
    backtrack = [[0]*(len(seq_two)+1) for _ in range(len(seq_one)+1)]
    high = -3*(len(seq_one)+len(seq_two))

    for i in range(1, len(seq_one)+1):
        for j in range(1, len(seq_two)+1):
            scores = [matrix[i-1][j-1] + get_score(seq_one[i-1], seq_two[j-1]),
                      matrix[i-1][j] - 2, matrix[i][j-1] - 2]
            matrix[i][j] = max(scores)
            backtrack[i][j] = scores.index(matrix[i][j])
            if i == len(seq_one) or j == len(seq_two):
                if matrix[i][j] > high:
                    high = matrix[i][j]
                    x, y = i, j

    one_aligned, two_aligned = seq_one[:x], seq_two[:y]

    indel = lambda word, i: word[:i] + '-' + word[i:]
    while x*y != 0:

        if backtrack[x][y] == 1:
            x -= 1
            two_aligned = indel(two_aligned, y)
        elif backtrack[x][y] == 2:
            y -= 1
            one_aligned = indel(one_aligned, x)
        else:
            x -= 1
            y -= 1

    one_aligned = one_aligned[x:]
    two_aligned = two_aligned[y:]

    return high, one_aligned, two_aligned


def overlap_alignment_setup(text):
    in_file = open(text)
    lines = in_file.read().strip().split("\n")

    seq_one = lines[0]
    seq_two = lines[1]

    score, seq1, seq2 = overlap_alignment(seq_one, seq_two)
    tmp = str(score)+"\n"+seq1+"\n"+seq2
    return tmp

print overlap_alignment_setup("rosalind_ba5i (3).txt")

