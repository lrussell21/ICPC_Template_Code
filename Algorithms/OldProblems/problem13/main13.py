import os
import copy
import sys
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.output = ''
        self.count = 0
        self.circuitCount = 0
        self.biColor = True
        self.colorMap = defaultdict(list)
        self.containsCycleBool = False
        self.visited = [False] * (self.V + 1)
        self.stack = []

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        #self.graph[v].append(u)

    def removeNode(self, graph, node):
        if node in graph:
            del graph[node]
        for x in graph:
            if node in graph.get(x):
                graph[x].remove(node)
        return graph

    def printGraph(self):
        print(self.graph)
        # for x in self.graph:
        #    print(x)


 
    def topologicalSort(self, v): 

        self.visited[v] = True
  
        for i in self.graph[v]: 
            if self.visited[i] == False: 
                self.topologicalSort(i)
  
        self.stack.insert(0,v) 



    def topologicalSortStart(self): 
        
        for i in range(1, self.V + 1):
            if self.visited[i] == False:
                self.topologicalSort(i)
        
        print(self.stack)



    def getDegree(self, vertex):
        try:
            return len(self.graph.get(str(vertex)))
        except:
            return -1

    def getAllVertexDegrees(self):
        out = []
        for index in range(len(self.graph)):
            out.append(self.getDegree(index + 1))
            #print(self.graph.get(str(index + 1)))
        return out

    def sumOfDegreeNeighbors(self):
        out = []
        for index in range(len(self.graph)):
            sum = 0
            for x in self.graph[str(index + 1)]:
                sum = sum + self.getDegree(x)
            out.append(sum)
        return out


def main():

    sys.setrecursionlimit(10000)

    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    graphs = []
    graphEdges = []
    numOfVerticies = 0
    skipFirstLine = True
    firstVals = True
    for x in numInput:
        if firstVals:
            numOfVerticies = x.split()[0]
            firstVals = False
        else:
            graphEdges.append(x.split())

    #print(numOfVerticies, " ", graphEdges)
    #for gr in graphs:
    #    print(gr)


    g = Graph(int(numOfVerticies))
    for x in graphEdges:
        g.addEdge(int(x[0]), int(x[1]))
    #g.printGraph()

    #print(g.visited)
    outputS = ""
    g.topologicalSortStart()
    for x in g.stack:
        outputS += str(x) + " "
    #print(outputS)




    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(outputS))


if __name__ == "__main__":
    main()
