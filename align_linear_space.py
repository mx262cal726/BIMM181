__author__ = 'Kyle'

def global_alignment_score(seq_one, seq_two, scoring_matrix, penalty):

    matrix = [[0 for _ in range(len(seq_two)+1)] for _ in range(len(seq_one)+1)]
    backtrack = [[0]*(len(seq_two)+1) for _ in range(len(seq_one)+1)]

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


def align_linear_space(seq1, seq2, scoring_matrix, penalty):
    def linear_alignment(top, bottom, left, right):
        if left == right:
            return [seq1[top:bottom],'-'*(bottom-top)]
        elif top == bottom:
            return ['-'*(right-left),seq2[left:right]]
        elif bottom - top == 1 or right - left == 1:
            return global_alignment_score(seq1[top:bottom], seq2[left:right],
                                          scoring_matrix, penalty)[1:]
        else:
            middle,  next_ = middle_edge(seq1[top:bottom],seq2[left:right],
                                        scoring_matrix, penalty)
            middle = tuple(map(sum, zip(middle, [top,left])))
            next_ = tuple(map(sum, zip(next_, [top,left])))
            current = [['-', seq1[middle[0]%len(seq1)]][next_[0] - middle[0]],
                       ['-',seq2[middle[1]%len(seq2)]][next_[1]-middle[1]]]
            A = linear_alignment(top, middle[0], left, middle[1])
            B = linear_alignment(next_[0], bottom, next_[1], right)
            return [A[i] + current[i] + B[i] for i in range(2)]
    seq1_aligned, seq2_aligned = linear_alignment(0, len(seq1), 0, len(seq2))
    score = sum([-penalty if '-' in pair else scoring_matrix[pair] for pair in zip(seq1_aligned, seq2_aligned)])
    return str(score),seq1_aligned, seq2_aligned

class Blosum62(object):

    def __init__(self, text):
        scoring_matrix = open(text)
        pairs = [line.strip().split() for line in scoring_matrix.readlines()]
        self.scoring_matrix = {(pair[0], pair[1]):int(pair[2]) for pair in pairs}

    def __getitem__(self, pair):
        return self.scoring_matrix[pair[0], pair[1]]

if __name__ == '__main__':
    in_file = open("rosalind_ba5l (2).txt")
    lines = in_file.read().split("\n")
    seq1 = lines[0]
    seq2 = lines[1]
    score, seq1, seq2 = align_linear_space(seq1, seq2, Blosum62("BLOSUM62"), 5)

    print score+"\n"+seq1+"\n"+seq2