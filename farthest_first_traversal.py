__author__ = 'kyle rouse'
import random

def farthest_first_traversals(data1,data):

    split_data = data[0].split(" ")
    dataPoint = map(float,split_data)
    farthestList = []
    min_list = []
    #print "Min:", min_center(data1,data),data1
    for i in range(0,len(data)):
        split_data = data[i].split(" ")
        m = len(split_data) - 1
        value = 0
        data2 = map(float, data[i].split(" "))
        #min_list.append(min_center(data2,data))
        for j in range(len(data1)):
            d1 = data1[j]
            while m > 0:
                value += farthest(d1,data2)
                m -= 1

        farthestList.append((value,data[i]))
    farthestList.sort()
    min_list.sort()
    t = map(float,"32.3 1.9 5.1 16.2 8.8".split(" "))
    s = map(float, "23.1 31.1 3.6 0.8 0.3".split(" "))



    return farthestList


def farthest_first_traversal(k,data):
    ran = random
    ranInt = ran.randint(0,len(data)-1)
    data2 = data[ranInt]
    centers = set()
    tmp = map(str,data2)
    tmp = " ".join(tmp)
    centers.add(tmp)

    while len(centers) < k:
        print len(centers),k
        dataPoint = farthest_point(data,centers)
        size = len(centers)
        print size, len(centers),dataPoint
        while size == len(centers):
            dataP = dataPoint.pop()
            for i in range(len(centers)):
                if centers.difference(dataP[1]):
                    dataP = dataPoint.pop()
            print dataPoint,"dataPoint"
            tmp = map(str,dataPoint)
            tmp = " ".join(tmp)
            print len(centers)
            centers.add(tmp)
            print len(centers)
    print centers
    return centers



def farthest_point(data,centers):
    tmp = []
    for i in data:
        val = 0
        for j in centers:

            val += farthest(i,map(float,j[1].split(" ")))
        tmp.append((val,i))
    tmp.sort()
    return tmp


def min_center(dataPoint, dataSet):

    min_list = []
    for point in dataSet:
        t = 0
        point = map(float,point.split(" "))
        if point == dataPoint:
            continue
        for i in range(len(point)):
            t += (dataPoint[i]-point[i])**2

        min_list.append((t,point))
    return min(min_list)


def farthest(data1, data2):
    sumAns = 0
    for i in range(len(data2)):
        sumAns += (data1[i]-data2[i])**2
    return sumAns**.5

def main(text):
    lines = open(text).read().split("\n")

    k_split = lines[0][0].split(" ")
    data = []
    for i in lines[1:]:
        data.append(map(float,i.split(" ")))

    k = int(k_split[0])

    answer = farthest_first_traversal(k, data)



    print lines[1]
    while k != 1:

        print answer.pop()
        k -= 1

if __name__ == '__main__':
    main("input")
