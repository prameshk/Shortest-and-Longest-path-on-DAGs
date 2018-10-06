'''
This script is written by Pramesh Kumar for directed acyclic graphs.
'''
import csv

location = ""

class Nodes:
    def __init__(self, tmpIn):
        self.nodeId = tmpIn
        self.inDegree = 0
        self.outDegree = 0
        self.order = 0
        self.inNodes = []
        self.outNodes = []
        self.slabels = {} # Shortest path labels when this node is the origin
        self.spreds ={} # # predecessors of shortest path when this node is the origin
        self.llabels = {}  # Longest path labels when this node is the origin
        self.lpreds = {}  # predecessors of shortest path when this node is the origin

class Edges:
    def __init__(self, tmpIn):
        self.fromNode = tmpIn[0]
        self.toNode = tmpIn[1]
        self.cost = float(tmpIn[2])


def readNetwork():
    f = open('network.csv', 'r')
    reader = csv.reader(f)
    for row in reader:
        if row[0] not in nodes:
            nodes[row[0]] = Nodes(row[0])
        if row[1] not in nodes:
            nodes[row[1]] = Nodes(row[1])
        edges[row[0], row[1]] = Edges(row)
        nodes[row[1]].inNodes.append(row[0])
        nodes[row[0]].outNodes.append(row[1])


def topologicalOrdering():
    for e in edges:
        nodes[e[1]].inDegree = nodes[e[1]].inDegree + 1
    order = 0
    SEL = [k for k, v in nodes.iteritems() if v.inDegree == 0]
    while SEL:
        i = SEL.pop(0)
        order = order + 1
        nodes[i].order = order
        for j in nodes[i].outNodes:
            nodes[j].inDegree = nodes[j].inDegree - 1
            if nodes[j].inDegree == 0:
                SEL.append(j)
    if order < len(nodes):
        print "the network has cycle(s)"





def shortestPath(origin):
    for i in nodes:
        nodes[origin].slabels[i] = float("inf")
        nodes[origin].spreds[i] = "NA"
    nodes[origin].slabels[origin] = 0
    nodes[origin].spreds[origin] = -1
    order = 1
    #orderedList = sorted(nodes, key=lambda x: nodes[x].order > nodes[origin].order)
    #orderedList.remove(origin)
    while (order < len(nodes)):
        order = order + 1
        j = [n for n,k in nodes.iteritems() if k.order == order][0]
        #j = orderedList.pop(0)
        for k in nodes[j].inNodes:
            if nodes[origin].slabels[j] > nodes[origin].slabels[k] + edges[k, j].cost:
                nodes[origin].slabels[j] = nodes[origin].slabels[k] + edges[k, j].cost
                nodes[origin].spreds[j] = k




def longestPath(origin):
    for i in nodes:
        nodes[origin].llabels[i] = -float("inf")
        nodes[origin].lpreds[i] = "NA"
    nodes[origin].llabels[origin] = 0
    nodes[origin].lpreds[origin] = -1
    order = 1
    #orderedList = sorted(nodes, key=lambda x: nodes[x].order > nodes[origin].order)
    #orderedList.remove(origin)
    while (order < len(nodes)):
        order = order + 1
        j = [n for n,k in nodes.iteritems() if k.order == order][0]
        #j = orderedList.pop(0)
        for k in nodes[j].inNodes:
            if nodes[origin].llabels[j] < nodes[origin].llabels[k] + edges[k, j].cost:
                nodes[origin].llabels[j] = nodes[origin].llabels[k] + edges[k, j].cost
                nodes[origin].lpreds[j] = k

def printShortestLongestPath(origin, dest):
    spreds = nodes[origin].spreds
    lpreds = nodes[origin].lpreds
    sp = [dest] # Shortest path
    lp = [dest] # Longest path
    currentNode = dest
    while spreds[currentNode] != origin:
        currentNode = spreds[currentNode]
        sp.append(currentNode)
    sp.append(origin)
    currentNode = dest
    while lpreds[currentNode] != origin:
        currentNode = lpreds[currentNode]
        lp.append(currentNode)
    lp.append(origin)
    print "Shortest path is ", list(reversed(sp)), "with cost", nodes[origin].slabels[dest]
    print "Shortest path is ", list(reversed(lp)), "with cost", nodes[origin].llabels[dest]



edges = {}
nodes = {}

readNetwork()
topologicalOrdering()
shortestPath('1')
longestPath('1')
printShortestLongestPath('1', '16')
