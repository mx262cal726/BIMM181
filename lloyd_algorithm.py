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


def center_of_gravity(points):
    center_dist = 0
    print points

    print "POINTS:", points[0][2][1]
    newCenter = [0]*len(points[0][2][1])
    tmp = 0
    size = 0
    prev = points[1]

    for j in range(len(points[0][2][1])):

        for i in range(len(points)):


            tmp += points[i][1][j]
            size += 1
            if prev != points[i]:
                print "tmp",tmp
                newCenter[j].append(tmp/float(size))
                tmp = 0
                size = 0
            else:
                prev = points[i][0][1]
                newCenter[j] = tmp/float(size)

    print "newCenter:",newCenter
    return newCenter


centersMap = {"centers":[]}


def add_center(center):
  centersMap["centers"].append(center)





def get_new_center(maps, centers):
    dist = 0
    length = len(centers[0].split(" "))
    newCenter = [0]*length
    tmp = [0]*length
    for i in range(len(maps)):
        currentPoints = maps[centers[i]]
        if len(currentPoints) == 0:

            tmp[i] = (map(float,centers[i].split(" ")))
            continue
        oldCenter = map(float,centers[i].split(" "))
        for l in range(len(oldCenter)):
            val = 0.0
            for j in currentPoints:
                point = map(float,j.split(" "))
                val += float(point[l])
            newCenter[l] = val/float(len(currentPoints))
        tmp[i]= newCenter
    return tmp




def lloyd_algorithm(data, k):
    centerKeys = [data[i] for i in range(k)]
    centers = [map(float, data[i].split(" ")) for i in range(k)]
    dataPoints = [map(float, data[i].split(" "))for i in range(k,len(data))]
    new_data = []
    new_data.append({i})
    maps = {data[0]:[]}
    for i in range(k):
        maps[data[i]] = []
    print maps


    for i in dataPoints:
        tmp =  " ".join([str(j) for j in i])
        cent = " ".join([str(j) for j in min_dist(i,centers)[1]])
        print cent
        maps[cent].append(tmp)
    while True:
        print maps, "new data", centers
        newCenters = get_new_center(maps,centerKeys)
        print newCenters,centers
        if newCenters == centers:
            return centers
        else:
            centers = newCenters
        print dataPoints
        maps = {" ".join(str(i) for i in centers[0]):[]}
        for i in range(k):
            maps[" ".join(str(i) for i in centers[0])] = []
        print maps

        for i in dataPoints:
            mdist = min_dist(i,centers)
            print mdist,i
            new_data.append((mdist, i))
        print "new data", new_data




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
    km = lines[0].split(" ")
    data = lines[1:]
    print lloyd_algorithm(data,int(km[0]))


if __name__ == '__main__':
    main("input")
