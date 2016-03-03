__author__ = 'Kyle Rouse'


def d(data1, data2):
    value = 0
    for i in range(len(data1)):
        value += (data1[i] - data2[i])**2

    return value**.5


def traversal_first_traversal(data, k):
    point = data[0]
    centers = []
    centers.append(point)
    data.remove(point)
    while len(centers) < k:
        dataSets = []
        for i in range(0, len(data)):
            min_distance = min_dist(data[i], centers)
            dataSets.append((min_distance, data[i]))

        center = max([i for i in dataSets], key=lambda x:x[0][0])
        centers.append(center[1])
        dataSets.remove(center)
        data.remove(center[1])
    return centers


def min_dist(point, centers):
    tmp = []
    dist = 0
    list_order = []
    for i in centers:
        if i != point:
            dist += d(point, i)
            list_order.append((d(point,i),i))
    tmp.append((i, dist))
    return min(list_order,key=lambda x:x[0])


def main(text):
    lines = open(text).read().split("\n")
    splitLine = lines[0].split(" ")
    k = float(splitLine[0])
    data = lines[1:]
    data = [map(float,i.split(" ")) for i in data]


    answer = traversal_first_traversal(data, k)

    for i in answer:
        for j in i:
            print j,

        print


if __name__ == '__main__':
    main("rosalind_ba8a.txt")
