__author__ = 'kyle rouse'


def main(text):
    lines = open(text).read().split("\n")
    km = lines[0].split(" ")
    k = int(km[0])
    m = int(km[1])
    data = [map(float, i.split(" ")) for i in lines[1:]]

    nodes = Nodes(k, m)
    for i in range(len(data)):
        if i < k:
            node = Node(data[i],lines[1+i], True, True)
        else:
            node = Node(data[i],lines[1+i], True, False)
        nodes.add(node)
    for i in range(len(data)):
        if nodes.get(i).isCenter:
            print nodes.get(i).key
            nodes.addCenter(nodes.get(i))

    oldSet = set(nodes.centers)
    newCentersSet = set()

    while oldSet != newCentersSet:
        newCenters = []
        for i in range(len(nodes.centers)):

            current = nodes.centers[i]
            newCenter = nodes.centerOfCluster(current)
            if newCenter.key != current.key:
                newCenters.append(newCenter)
            else:
                newCenters.append(current)

        oldSet = {i.key for i in nodes.centers}
        nodes.clearCenters()

        for i in range(k):
            nodes.addCenter(newCenters[i])
        newCentersSet =  { i.key for i in newCenters}


    for i in range(len(nodes.centers)):
        print nodes.centers[i].key


class Nodes(object ):
    def __init__(self, k, m):
        self.nodes = []
        self.centers = []
        self.m = m
        self.k = k
        self.centersMap = {}

    def centerOfCluster(self, oldCenter):
        tmp = []
        key = oldCenter.key
        for i in range(self.m):
            total = 0
            for j in range(len(self.centersMap[key])):
                total += self.centersMap[key][j][i]
            total = total*(1.0/float(len(self.centersMap[key])))
            tmp.append(round(total,3))

        return Node(tmp, self.toString(tmp), False, True)

    def clearCenters(self):
        for i in range(self.size()):
            self.nodes[i].clearCenter()
        self.centers = []
        self.centersMap = {}


    def addCenter(self, node):
        self.centers.append(node)
        self.updateCenter(node)
        self.setupMap()
        self.updateMap()

    def printCenters(self):
        for i in range(len(self.centers)):
            print "Center:",self.centers[i].key,"Size",len(self.centersMap[self.centers[i].key])
            print "----------------------------"
            for j in range(len(self.centersMap[self.centers[i].key])):
                print self.centers[i].key,
                print self.centersMap[self.centers[i].key][j]
            print "----------------------------"

    def setupMap(self):
        for i in range(len(self.centers)):
            self.centersMap[self.centers[i].key] = []

    def updateMap(self):

        for i in range(self.size()):
            key = self.get(i).clusterHome
            if self.centersMap.has_key(key):
                self.centersMap[key].append(self.get(i).point)


    def updateCenter(self,center):
        for i in range(self.size()):
            if len(self.centers) <= 1:
                self.get(i).clusterHome = self.toString(center.point)
                self.get(i).updateDist(self.distance(i, center))
            else:
                currentDist = self.get(i).distToCenter
                newDist = self.distance(i,center)
                if newDist < currentDist:
                    self.get(i).clusterHome = self.toString(center.point)
                    self.get(i).updateDist(newDist)


    def toString(self,data):
        return " ".join(str(i) for i in data)

    def printNodes(self):
        for i in range(self.size()):
            self.nodes[i].printNode()

    def distance(self, index, center):
        value = 0.0
        node = self.get(index)
        for i in range(self.m):
            value += (node.point[i]-center.point[i])**2
        return value**.5

    def add(self, node):
        self.nodes.append(node)

    def get(self,i):
        return self.nodes[i]

    def size(self):
        return len(self.nodes)


class Node():
    def __init__(self, point, key, original, center):
        self.point = point
        self.key = key
        self.original = original
        self.isCenter = center
        self.clusterHome = key
        self.distToCenter = 0.0

    def updateDist(self, distance):
        self.distToCenter = distance

    def clearCenter(self):
        self.isCenter = False
        self.clusterHome = self.key
        self.distToCenter = 0.0

    def printNode(self):
        if self.isCenter:
            print "-----CENTER-----"
        print "Point:   ", self.point,
        print "Key:       ", self.key
        print "Original:", self.original,
        print "      isCenter:  ", self.isCenter
        print "Distance:",self.distToCenter
        print "Cluster: ",self.clusterHome
        print "----------------------------------------"



if __name__ == '__main__':
    main("rosalind_ba8c (1).txtk")
