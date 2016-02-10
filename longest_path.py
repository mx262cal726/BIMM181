__author__ = 'kyle'


def longest_path_setup(text):
    file_in = open(text)
    lines_list = file_in.read().split("\n")

    dimensions = lines_list[0].split(" ")
    m1, m2 = get_matrices(lines_list[1:len(lines_list)])
    n = int(dimensions[0])
    m = int(dimensions[1])

    return longest_path(n, m, m1, m2)


def longest_path(n, m, down, right):

    zero_matrix = [[0]*(m+1) for i in range(n+1)]

    for i in range(1, n+1):
        zero_matrix[i][0] = zero_matrix[i-1][0] + down[i-1][0]

    for i in range(1, m+1):
        zero_matrix[0][i] = zero_matrix[0][i-1] + right[0][i-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            zero_matrix[i][j] = max(zero_matrix[i-1][j]+down[i-1][j], zero_matrix[i][j-1] + right[i][j-1])
    return zero_matrix[n][m]


def get_matrices(matrix_list):
    matrix = list()
    matrix_container = list()
    for i in range(0, len(matrix_list)):
        weights = matrix_list[i].split(" ")
        node = list()
        if matrix_list[i] != "-":
            for j in range(0, len(weights)):
                node.append(int(weights[j]))
            matrix.append(node)

        else:
            matrix_container.append(matrix)
            matrix = list()

    matrix_container.append(matrix)
    return matrix_container[0], matrix_container[1]


print longest_path_setup("input")
