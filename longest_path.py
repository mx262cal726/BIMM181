__author__ = 'kyle'

<<<<<<< HEAD

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
=======
def longest_path(text):
    file_in = open(text)
    lines_list = file_in.read().split("\n")
    dimensions = lines_list[0].split(" ")
    x = dimensions[0]
    y = dimensions[1]
    x_dim = int(x)-1
    y_dim = int(y)-1
    nodes_matrix = Nodes(0, list(), len(lines_list[1]), 0)
    matrix_container = list()
    matrix = nodes_matrix.matrix
    dim_y = 0
    max = 0
    for i in range(1, len(lines_list)):
        weights_list = lines_list[i].split(" ")
        tmp_path = ""
        tmp_max = 0
        if lines_list[i] != "-":
            length = len(weights_list)
            matrix.append(list()*length)
            y = nodes_matrix.get_y()
            node = matrix[y]
            for j in range(0, length):
                weight = int(weights_list[j])
                if y == 0:
                    if j == 0:
                        tmp_max = weight
                        node.append(Node(weight,weight,weight))
                    else:
                        tmp_max = weight+node[j-1].get_max()
                        node.append(Node(weight,weight,weight+node[j-1].get_max()))

                else:
                    if j == 0:
                        tmp_max = weight+matrix[y-1][j].get_max()
                        node.append(Node(weight,tmp_max,weight))
                    else:
                        left_weight = weight+node[j-1].get_max()

                        top_weight = weight+ matrix[y-1][j].get_max()

                        node.append(Node(weight,left_weight,top_weight))

                        tmp_max = node[j].get_max()

                tmp_path += str(weight)+","
                print "TMP MAX:",tmp_max
                if tmp_max > nodes_matrix.max_weight:
                    nodes_matrix.max_weight = tmp_max
                    nodes_matrix.set_max_weight(tmp_max)
            nodes_matrix.set_y(nodes_matrix.get_y()+1)

        else:
            if nodes_matrix.matrix[x_dim][y_dim].get_max() > max:
                max = nodes_matrix.matrix[x_dim][y_dim].get_max()
            nodes_matrix.print_matrix()
            matrix_container.append(nodes_matrix)
            nodes_matrix.set_y(0)
            nodes_matrix = Nodes(0, list(), len(lines_list[1]), 0)
            matrix = nodes_matrix.matrix
    matrix_container.append(nodes_matrix)
    return max


class Nodes:
    def __init__(self, weight, matrix, x, y):
        #self.nodes = nodes
        self.max_weight = weight
        self.matrix = matrix
        self.x = x
        self.y = y
        self.target = weight

    def set_target(self,in_weight):
        if self.target < in_weight:
            self.target = in_weight


    def get_target(self):
        return self.target

    def get_x(self):
        return self.x

    def print_matrix(self):
        for i in range(0,len(self.matrix)):
            row = ""
            for j in range(0, len(self.matrix[i])):
                row += str(self.matrix[i][j].get_max())+" "
            print row

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_max_weight(self):
        return self.max_weight

    def set_max_weight(self,weight):
        self.max_weight = weight

    def add_row(self, row):
        self.y += 1
        self.matrix.append(row)


    def add_node(self,node):
        self.nodes.append(node)


class Node:
    def __init__(self, weight, top_weight, left_weight):
        self.weight = weight
        if top_weight > left_weight:
            self.total_weight_max = top_weight
        else:
            self.total_weight_max = left_weight
        self.total_weight_top = top_weight
        self.total_weight_left = left_weight

    def top_total(self):
        return self.total_weight_top

    def set_top_total(self, weight):
        if weight > self.total_weight_max:
            self.total_weight_max = int(weight)
        self.total_weight_top = int(weight)

    def set_left_total(self,weight):
        if weight > self.total_weight_max:
            self.total_weight_max = int(weight)
        self.total_weight_top = int(weight)

    def left_total(self):
        return self.total_weight_left

    def get_max(self):
        return self.total_weight_max

    def set_max(self, weight):
        self.total_weight_max = int(weight)

print longest_path("input.txt")
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
