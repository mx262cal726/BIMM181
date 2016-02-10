__author__ = 'kyle'


def global_alignment_score(v, w, scoring_matrix, sigma):
    '''Return the global alignment score of v and w subject to the given scoring matrix and indel penalty sigma.'''

    # Initialize the scoring matrix.
    S = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    print S
    # Initialize the edges with the given penalties.
    for i in xrange(1, len(v)+1):
        S[i][0] = -i*sigma
    for j in xrange(1, len(w)+1):
        S[0][j] = -j*sigma

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]]]
            S[i][j] = max(scores)

    return S[len(v)][len(w)]

import ReadFASTA

if __name__ == '__main__':

    # Parse the two input protein strings.
    ReadFASTA('input')

    # Get the alignment score.
    score = str(global_alignment_score(s, t, "BLOSUM62.txt", 5))

    # Print and save the answer.
    print score
    with open('output/069_GLOB.txt', 'w') as output_data:
        output_data.write(score)



def get_matrix(matrix):
    in_file = open(matrix)
    lines = in_file.read().split("\n")

    scores = lines[0].strip(" ").split()
    score_matrix = [[0]*(len(scores)+1) for i in range(len(lines)+1)]
    row = list()
    for i in range(0, len(scores)):
        score_matrix[0][i+1] = scores[i]
        score_matrix[i+1][0] = scores[i]
    for i in range(1, len(lines)):
        score = lines[i].replace("  "," ").split(" ")
        for j in range(1, len(scores)):
            score_matrix[i][j] = score[j]

    return score_matrix


def setup_global_alignment(score_matrix, text):
    in_file = open(text)

    scoring_matrix = get_matrix(score_matrix)
    lines = in_file.read().split("\n")
    seq_one = lines[0]
    seq_two = lines[1]

    return global_alignment_score(seq_one, seq_two, scoring_matrix, 5)


print setup_global_alignment("BLOSUM62.txt","input")