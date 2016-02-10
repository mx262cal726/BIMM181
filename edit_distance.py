__author__ = 'kyle'


def edit_distance(seq_one, seq_two):

    matrix = [[0 for _ in range(len(seq_two)+1)] for _ in range(len(seq_one)+1)]
    one_length = len(seq_one)
    two_length = len(seq_two)
    for i in range(1, one_length+1):
        matrix[i][0] = i

    for i in range(1, two_length+1):
        matrix[0][i] = i

    for i in range(1, one_length+1):
        for j in range(1, two_length+1):
            if seq_one[i-1] == seq_two[j-1]:
                score = matrix[i-1][j-1]
            else:
                score = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])+1
            matrix[i][j] = score
    return matrix[one_length][two_length]


def edit_distance_setup(text):
    in_file = open(text)
    lines = in_file.read().split("\n")

    seq_one = lines[0]
    seq_two = lines[1]

    score = edit_distance(seq_one, seq_two)
    return score

print edit_distance_setup("rosalind_ba5g.txt")

