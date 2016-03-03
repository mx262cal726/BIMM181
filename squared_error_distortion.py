__author__ = 'kyle rouse'


def squared_error_distortion(data):
    centers = data[0]
    dataPoints = data[1]
    value = 0

    for i in dataPoints:
        val = 0
        for j in centers:

            val += farthest(map(float,j.split(" ")),map(float,i.split(" ")))
        value += val**2
    print value*(1.0/len(dataPoints))


def farthest(data1, data2):
    sumAns = []
    for i in range(len(data2)):
        sumAns.append((data1[i]-data2[i])**2)
    return min(sumAns)**.5


def main(text):
    lines = open(text).read().split("\n")
    km = lines[0]
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
    print store


if __name__ == '__main__':
    main("input")
