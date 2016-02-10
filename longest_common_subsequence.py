__author__ = 'kyle'


def longest_common_subsequence(seq_one, seq_two):

    matrix = get_manhattan_graph(seq_one, seq_two)
    longest_seq = ""
    one_length = len(seq_one)
    two_length = len(seq_two)
    while one_length != 0 and two_length != 0:
        if matrix[one_length][two_length] == matrix[one_length-1][two_length]:
            one_length -= 1
        elif matrix[one_length][two_length] == matrix[one_length][two_length-1]:
            two_length -= 1
        else:
            longest_seq = seq_one[one_length-1] + longest_seq
            one_length -= 1
            two_length -= 1

    return longest_seq


def get_manhattan_graph(seq_one, seq_two):
    zero_matrix = [[0]*(len(seq_two)+1) for i in range(len(seq_one)+1)]
    for i in range(len(seq_one)):
        for j in range(len(seq_two)):
            if seq_one[i] == seq_two[j]:
                zero_matrix[i+1][j+1] = zero_matrix[i][j]+1
            else:
                zero_matrix[i+1][j+1] = max(zero_matrix[i+1][j], zero_matrix[i][j+1])
    return zero_matrix


def setup_longest_subsequence(text):
    in_file = open(text)
    lines = in_file.read().split("\n")
    seq_one = lines[0]
    seq_two = lines[1]

    return longest_common_subsequence(seq_one, seq_two)


print setup_longest_subsequence("input")