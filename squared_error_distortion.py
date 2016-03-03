__author__ = 'kyle rouse'


def d(data1, data2):
    value = 0
    for i in range(len(data1)):
        value += (data1[i] - data2[i])**2
    return value


def squared_error_distortion(data):

    centers = [map(float, i.split(" ")) for i in data[0]]
    dataPoints = [map(float, i.split(" "))for i in data[1]]
    distance = 0
    for i in dataPoints:
        mdist = min_dist(i,centers)
        distance += mdist[0]

    return distance*(1.0/len(dataPoints))


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


def farthest(data1, data2):
    sumAns = []
    for i in range(len(data2)):
        sumAns.append((data1[i]-data2[i])**2)
    return min(sumAns)**.5


def main(text):
    lines = open(text).read().split("\n")
    centers = []
    store = []
    for i in lines[1:]:
        if i == "--------":
            store.append(centers)
            centers = []
            continue
        centers.append(i)

    store.append(centers)
    print squared_error_distortion(store)


if __name__ == '__main__':
    main("rosalind_ba8b.txt")
