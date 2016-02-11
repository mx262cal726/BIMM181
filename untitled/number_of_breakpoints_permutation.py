__author__ = 'Kyle'


def number_of_breakpoints(text):
    order = map(int,list(text.split(" ")))
    breaks = 0
    if order[0] != 1:
        breaks += 1
    for i in range(1, len(order)):
        if order[i] - order[i-1] != 1:
            breaks += 1
    return breaks


def main():
    in_file = open("rosalind_ba6b.txt").read().split("\n")
    print number_of_breakpoints(in_file[0].strip("()"))


if __name__ == '__main__':
    main()
