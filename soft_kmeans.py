__author__ = 'kyle rouse'
import math

def generateNewCenters(nodes):
    newCenters = []
    for i in range(len(nodes.centers)):
            current = nodes.centers[i]
            newCenter = nodes.centerOfCluster(current,i)
            if newCenter.key != current.key:
                newCenters.append(newCenter)
                nodes.addCurrentCenter(newCenter)
            else:
                newCenters.append(current)
    oldSet = {i.key for i in nodes.centers}
    nodes.clearCenters()
    return oldSet, newCenters

def generateNewClusters(nodes, newCenters, k):
    for i in range(k):
        nodes.addCenter(newCenters[i],i)
    newCentersSet = {i.key for i in newCenters}
    return newCentersSet

def main(text):
    lines = open(text).read().split("\n")
    km = lines[0].split(" ")
    k = int(km[0])
    m = int(km[1])
    stiffness = float(lines[1])
    data = [map(float, i.split(" ")) for i in lines[2:]]
    nodes = Nodes(k, m)
    nodes.setStiffness(stiffness)
    for i in range(len(data)):
        if i < k:
            node = Node(data[i],lines[2+i], True, True)
        else:
            node = Node(data[i],lines[2+i], True, False)
        nodes.add(node)
    for i in range(len(data)):
        if nodes.get(i).isCenter:
            nodes.addCenter(nodes.get(i), i)
            nodes.get(i).promoteToCenter()
    nodes.setupResponsibilities()

    nodes.setMemberships()
    nodes.setupRMatrix()
    nodes.responsibilityMatrix()

    oldCenters = set(nodes.centers)
    newCentersSet = set()
    count = 0
    while oldCenters != newCentersSet or count > 10:

        oldCenters, newCenters = generateNewCenters(nodes)
        newCentersSet = generateNewClusters(nodes, newCenters, k)
        count += 1

    nodes.hiddenMatrix()
    for i in nodes.hiddenMatrix():
        print i
    for i in range(len(nodes.centers)):
        print nodes.centers[i].key




class Nodes(object ):
    def __init__(self, k, m):
        self.nodes = []
        self.centers = []
        self.m = m
        self.k = k
        self.centersMap = {}
        self.distToAll = {}
        self.hiddenM = []
        self.beta = 0
        self.e = 2.72
        self.one = []
        self.allM = {}
        self.rMatrix = {}
        self.currentCenters = []


    def theta(self):
        tmp = 0
        count = 0
        for i in self.nodes:
            print "i", self.centers[0].key
            print "i.clusterHome",i.clusterHome
            if i.clusterHome == self.centers[0].key:
                tmp += i.distToCenter
                count += 1
        print tmp/count

    def addCurrentCenter(self,center):
        self.currentCenters.append(center)

    def cSize(self):
        return len(self.centers)


    def setupResponsibilities(self):
        for i in range(self.size()):
            for j in range(len(self.centers)):
                self.get(i).setResponse(self.centers[j].key,self.hiddenMatrix()[self.centers[j].key][i],self.centers)


    def weightedCenters(self,index):
        tmp = []
        center = []
        for i in range(self.m):
            numerator = 0
            denominator = 0

            for j in range(self.size()):
                numerator += self.get(j).point[i]*self.hiddenMatrix()[index][j]
                denominator += self.hiddenMatrix()[index][j]
            center.append(round(numerator/denominator,3))
            tmp.append(round(numerator/denominator,3))
        wcenter = Node(tmp,self.toString(tmp),False,True)
        #del self.centersMap[self.centers[index].key]
        #self.centers.remove(self.centers[i])
        self.addCurrentCenter(wcenter)
        self.addCenter(wcenter, index)
        return tmp

    def setStiffness(self,s):
        self.beta = -s

    def setupRMatrix(self):
        for i in range(len(self.centers)):
            self.rMatrix[self.centers[i].key] = {j.key:[] for j in self.nodes}

    def dotProduct(self, index, m):
        val = 0.0
        denominator = 0.0
        if self.rMatrix.has_key(self.centers[index].key):

            for i in range(len(self.rMatrix[self.centers[index].key])):
                print self.rMatrix[self.centers[index].key][self.get(i).key]
                val += self.rMatrix[self.centers[index].key][self.get(i).key]*self.get(i).point[m]
                denominator += self.rMatrix[self.centers[index].key][self.get(i).key]
            print "denominator",denominator,val
            return round(val/denominator,3)
        else:
            return 1

    def mStep(self):
        tmp = []
        for i in range(len(self.centers)):
            val = []
            for j in range(self.m):
                val.append(self.dotProduct(i, j))
            tmp.append(val)
        return tmp

    def responsibilityMatrix(self):
        responsibility=lambda beta,d: math.exp(beta * d)
        for i in range(len(self.centers)):
            for j in range(self.size()):
                numerator = responsibility(self.beta,self.distance(j,self.centers[i]))
                denominator = self.denominator(j)
                self.rMatrix[self.centers[i].key][self.get(j).key] = round(numerator/denominator,3)

    def one_matrix(self):
        one = [[0 for _ in range(self.k)] for _ in range(self.size())]
        for i in range(self.size()):
            tmp = []
            t = 0.0
            index = 0
            for j in range(self.k):
                if self.hiddenMatrix()[j][i] > t:
                    t = self.hiddenMatrix()[j][i]
                    index = j
            one[i][index] = 1
        self.one = one

    def hiddenMatrix(self):
        matrix = {i.key:[] for i in self.centers}
        responsibility=lambda beta,d: math.exp(beta * d)
        for i in range(len(self.centers)):
            tmp = []
            for j in range(self.size()):

                distance = self.distance(j,self.centers[i])
                numerator = responsibility(self.beta, distance)
                denominator = self.denominator(j)
                tmp.append(round(numerator/denominator,3))
                matrix[self.centers[i].key].append(round(numerator/denominator,3))
        return matrix


    def dot(self, i):
        numerator = 0
        denominator = 0
        ans = []
        for index in range(self.m):
            for j in range(self.size()):
                numerator += self.get(j).point[index]*self.hiddenMatrix()[i][index]
                denominator += self.hiddenMatrix()[i][j]
            ans.append(round(numerator/denominator, 3))
        return ans

    def denominator(self,i):
        responsibility=lambda beta,d: math.exp(beta * d)
        tmp = 0
        for j in range(len(self.centers)):
            tmp += responsibility(self.beta,self.distance(i,self.centers[j]))
        return tmp

    def centerOfCluster(self, oldCenter,index):
        tmp = []
        key = oldCenter.key
        for i in range(self.m):
            total = 0
            for j in range(len(self.centersMap[key])):
                total += self.centersMap[key][j].point[i]
            total = total*(1.0/float(len(self.centersMap[key])))
            tmp.append(round(total,3))
        print self.mStep()
        return Node(tmp, self.toString(tmp), False, True)

    def clearCenters(self):
        for i in range(self.size()):
            self.nodes[i].clearCenter()
        self.centers = []
        self.centersMap = {}
        self.distToAll = {}

    def setDistToAll(self, node, index):
        self.distToAll[node.key] = {i.key:[] for i in self.centers}
        for i in range(self.size()):
            if self.get(i).isOriginal:
                self.distToAll[node.key][self.get(i).key] = round(self.distance(i,node),3)

    def addCenters(self,node,i):
        self.setDistToAll(node,i)
        self.centers.append(node)
        self.addPoints(node,i)

    def addPoints(self,node,i):
        for i in range(self.size()):
            key = self.get(i).clusterHome
            if self.centersMap.has_key(key):
                self.centersMap[key].append(self.get(i))


    def addCenter(self, node, i):
        self.setDistToAll(node, i)
        self.centers.append(node)
        self.updateCenter(node,i)
        self.setupMap()
        self.updateMap()


    def setMemberships(self):
        val = 0.0

        for i in range(self.size()):
            if self.get(i).isCenter == False:
                for center in range(len(self.centers)):
                    for rc in range(len(self.centers)):
                        if self.get(i) is not self.centers[rc]:
                            distToCenter = self.distance(i,self.centers[center])
                            distToOther = self.distance(i, self.centers[rc])
                            val += (distToCenter/float(distToOther))**(2.0/(float(self.k)-1.0))
                    self.get(i).setM(self.centers[center].key, round(val**-1,5))
                    self.allM[self.get(i).key] = {self.centers[center].key:val}

                print "MEMBERSHIP:", self.get(i).membership

    def printCenters(self):
        for i in range(len(self.centers)):
            print "Center:",self.centers[i].key,"Size",len(self.centersMap[self.centers[i].key])
            print "----------------------------"
            for j in range(len(self.centersMap[self.centers[i].key])):
                print self.centers[i].key,
                print self.centersMap[self.centers[i].key][j].key
            print "----------------------------"

    def printAllResponseibilities(self):
        for i in self.centers:
            print "Centers:", i.key
        for i in range(self.size()):
            self.get(i).printResponsibilities(self.centers)

    def setupMap(self):
        for i in range(len(self.centers)):
            self.centersMap[self.centers[i].key] = []

    def updateMap(self):

        for i in range(self.size()):
            for j in range(len(self.centers)):
                key = self.centers[j].key
                self.centersMap[key].append(self.get(i))

    def upgradeToCenter(self, center, index):
        tmp = []

        for c in range(len(self.centers)):
            for i in range(self.size()):
                print self.centers[c].key
                if self.get(i).isCenter == False or self.get(i) == self.centers[c]:
                    self.centersMap[self.centers[c].key].append(self.get(i))


    def updateCenter(self,center,index):
        for i in range(self.size()):
            for c in range(len(self.centers)):
                if self.get(i).isCenter == False or self.get(i).key == center.key:
                    self.get(i).clusterHome = self.toString(center.point)
                    self.get(i).updateDist(self.distance(i, center))

    def toString(self,data):
        return " ".join(str(i) for i in data)

    def printNodes(self):
        for i in range(self.size()):
            self.nodes[i].printNode()

    def distance(self, index, center):
        value = 0.0
        node = self.get(index)
        for i in range(self.m):
            value += (node.point[i]-center.point[i])**2.0
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
        self.membership = {}
        self.responsibility = {}

    def d(self):
        return self.distToCenter

    def setM(self, key, membership):
        self.membership[key] = membership

    def isOriginal(self):
        return self.original

    def getR(self):
        return self.responsibility

    def printResponsibilities(self,centers):
        for i in range(len(self.responsibility)):
            print "ClusterHome: ",self.clusterHome, "Data Point:",self.key
            print "Center:      ",centers[i].key
            print "Responsibity:",self.responsibility[centers[i].key]
        print "------------------------------------"

    def setResponse(self, key, value, centers):
        for i in range(len(centers)):
            self.responsibility[key] = [value]

    def updateResponse(self):
        for i in range(self.size()):
            key = self.get(i).clusterHome
            if self.centersMap.has_key(key):
                self.centersMap[key].append(self.get(i))



    def promoteToCenter(self):
        self.clusterHome = self.key
        self.isCenter = True
        self.distToCenter = 0.0

    def updateCenter(self, point,key):
        self.point = point
        self.key = key

    def updateDist(self, distance):
        self.distToCenter = distance

    def clearCenter(self):
        self.isCenter = False
        self.clusterHome = self.key
        self.distToCenter = 0.0
        self.responsibility = {}

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
    main("input")
