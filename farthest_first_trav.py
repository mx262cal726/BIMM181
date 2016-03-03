__author__ = 'Kyle Rouse'


def d(data1, data2):
    value = 0
    for i in range(len(data1)):
        value += (data1[i] - data2[i])**2
    return value**.5


def traversal_first_traversal(data, k):
    point = data[0]
    dataSets = []
    centers = []
    centers.append(point)
    data.remove(point)
    print "point",point
    while len(centers) < k:
        for i in range(0, len(data)):
            dataSets.append((min_dist(data[i], centers), data[i]))
        center = max([i for i in dataSets], key=lambda x:x[0][1])

        centers.append(center[1])
        dataSets.remove(center)
        data.remove(center[1])
    print "Centers:",centers



def min_dist(point, centers):
    tmp = []
    dist = 0
    for i in centers:
        if i != point:
            dist += d(point, i)

    tmp.append((i, dist))
    return min(tmp)


def main(text):
    lines = open(text).read().split("\n")
    splitLine = lines[0].split(" ")
    k = float(splitLine[0])
    data = lines[1:]
    data = [map(float,i.split(" ")) for i in data]

    print traversal_first_traversal(data, k)


if __name__ == '__main__':
    print main("input")