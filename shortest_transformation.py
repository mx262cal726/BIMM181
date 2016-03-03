__author__ = 'kyle rouse'


def burrows_wheeler_transform(word):

    word += ['', '$'][word[-1] != '$']
    L = len(word)
    cyclic_rot_index = lambda i, n: word[(n-i) % L]
    cyclic_comp = lambda i, j, n=0: [1, -1][cyclic_rot_index(i,n) < cyclic_rot_index(j,n)] if cyclic_rot_index(i,n) != cyclic_rot_index(j,n) else cyclic_comp(i,j,n+1)
    cyclic_sort = sorted(xrange(len(word)), cmp=cyclic_comp)
    return ''.join([cyclic_rot_index(i,-1) for i in cyclic_sort])

def main(text):
    lines = open(text).read().split("\n")
    print lines


if __name__ == '__main__':
    main("input")
