__author__ = 'Kyle'


def middle_score(seq1, seq2, score_matrix, penalty):
    matrix = [[i*j*penalty for j in xrange(-1, 1)] for i in xrange(len(seq1)+1)]
    matrix[0][1] = -penalty
    backtrack = [0]*(len(seq1)+1)

    for j in xrange(1, len(seq2)/2+1):
        for i in xrange(0, len(seq1)+1):
            if i == 0:
                matrix[i][1] = -j*penalty
            else:
                scores = [matrix[i-1][0] + score_matrix[seq1[i-1], seq2[j-1]], matrix[i][0] - penalty,
                          matrix[i-1][1] - penalty]
                matrix[i][1] = max(scores)
                backtrack[i] = scores.index(matrix[i][1])
        if j != len(seq2)/2:
            matrix = [[row[1]]*2 for row in matrix]

    return [row[1] for row in matrix], backtrack


def middle_edge(seq1, seq2, scoring_matrix, penalty):
    source_middle = middle_score(seq1, seq2, scoring_matrix, penalty)[0]
    middle_sink, backtrack = map(lambda l: l[::-1], middle_score(seq1[::-1],
            seq2[::-1]+['', '$'][len(seq2) % 2 == 1 and len(seq2) > 1], scoring_matrix, penalty))
    scores = map(sum, zip(source_middle, middle_sink))
    max_middle = max(xrange(len(scores)), key=lambda i: scores[i])
    if max_middle == len(scores) - 1:
        next_node = (max_middle, len(seq2)/2 + 1)
    else:
        next_node = [(max_middle + 1, len(seq2)/2 + 1), (max_middle, len(seq2)/2 + 1),
                     (max_middle + 1, len(seq2)/2),][backtrack[max_middle]]

    return (max_middle, len(seq2)/2), next_node


class Blosum62(object):

    def __init__(self, text):
        score_file = open(text)
        pairs = [line.strip().split() for line in score_file.readlines()]
        self.scoring_matrix = {(pair[0], pair[1]): int(pair[2]) for pair in pairs}

    def __getitem__(self, pair):
        return self.scoring_matrix[pair[0], pair[1]]


if __name__ == '__main__':
    in_file = open("input")
    lines = in_file.read().split("\n")
    seq1 = lines[0]
    seq2 = lines[1]
    scoring_matrix = Blosum62("BLOSUM62")
    print middle_edge(seq1, seq2, scoring_matrix, 5)
