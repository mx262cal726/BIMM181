
def multiple_common_subsequence(seq1, seq2, seq3):
    matrix = [[[0 for k in xrange(len(seq3)+1)] for j in xrange(len(seq2)+1)] for i in xrange(len(seq1)+1)]
    backtrack = [[[0 for k in xrange(len(seq3)+1)] for j in xrange(len(seq2)+1)] for i in xrange(len(seq1)+1)]

    for i in xrange(1, len(seq1)+1):
        for j in xrange(1, len(seq2)+1):
            for k in xrange(1, len(seq3)+1):
                scores = [matrix[i-1][j-1][k-1] + int(seq1[i-1] == seq2[j-1] == seq3[k-1]),matrix[i-1][j][k],
                          matrix[i][j-1][k], matrix[i][j][k-1], matrix[i-1][j][k-1], matrix[i][j-1][k-1]]
                backtrack[i][j][k], matrix[i][j][k] = max(enumerate(scores), key=lambda p: p[1])

    indel = lambda text, i: text[:i]+'-'+text[i:]
    i, j, z = len(seq1), len(seq2), len(seq3)
    max_score = matrix[i][j][z]
    seq1_aligned, seq2_aligned, seq3_aligned = seq1, seq2, seq3

    while i*j*z != 0:
        if backtrack[i][j][z] == 1:
            i -= 1
            seq2_aligned = indel(seq2_aligned, j)
            seq3_aligned = indel(seq3_aligned, z)
        elif backtrack[i][j][z] == 2:
            j -= 1
            seq1_aligned = indel(seq1_aligned, i)
            seq3_aligned = indel(seq3_aligned, z)
        elif backtrack[i][j][z] == 3:
            z -= 1
            seq1_aligned = indel(seq1_aligned, i)
            seq2_aligned = indel(seq2_aligned, j)
        elif backtrack[i][j][z] == 4:
            i -= 1
            j -= 1
            seq3_aligned = indel(seq3_aligned, z)
        elif backtrack[i][j][z] == 5:
            i -= 1
            z -= 1
            seq2_aligned = indel(seq2_aligned, j)
        elif backtrack[i][j][z] == 6:
            j -= 1
            z -= 1
            seq1_aligned = indel(seq1_aligned, i)
        else:
            i -= 1
            j -= 1
            z -= 1

    while len(seq1_aligned) != max(len(seq1_aligned), len(seq2_aligned), len(seq3_aligned)):
        seq1_aligned = indel(seq1_aligned, 0)

    while len(seq2_aligned) != max(len(seq1_aligned), len(seq2_aligned), len(seq3_aligned)):
        seq2_aligned = indel(seq2_aligned, 0)

    while len(seq3_aligned) != max(len(seq1_aligned), len(seq2_aligned), len(seq3_aligned)):
        seq3_aligned = indel(seq3_aligned, 0)

    return str(max_score), seq1_aligned, seq2_aligned, seq3_aligned

if __name__ == '__main__':
    in_file = open("rosalind_ba5m.txt")
    lines = in_file.read().strip().split("\n")
    seq1 = lines[0]
    seq2 = lines[1]
    seq3 = lines[2]
    score, seq1, seq2, seq3 = multiple_common_subsequence(seq1, seq2, seq3)

    print score+"\n"+seq1+"\n"+seq2+"\n"+seq3