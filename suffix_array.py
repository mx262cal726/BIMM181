__author__ = 'kyle rouse'


def get_btw(text):

    itext = lambda x: text[-1]+text[:-1]
    m = []
    for i in range(0, len(text)):
        m.append(text)
        text = itext(text)
    m.sort()
    return m


def suffix_array(text):
    bwList = get_btw(text)
    suffixArray = []
    for i in range(0,len(bwList)):
        for j in range(1, len(bwList)+1):
            if bwList[i][-j] == '$':
                suffixArray.append(j-1)
    return suffixArray


def main(text):
    lines = open(text).read().split("\n")
    pass




if __name__ == '__main__':
    main("input")
