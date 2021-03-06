import os 
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.output = ''

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

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
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    graphEdges = []
    numOfVerticies = 0
    firstVals = True
    for x in numInput:
        if firstVals:
            numOfVerticies = x[0]
            firstVals = False
        else:
            graphEdges.append(x.split())

    g = Graph(int(numOfVerticies) - 1)
    for x in graphEdges:
        #print(x[0], x[1])
        g.addEdge(x[0], x[1])

    outlist = g.sumOfDegreeNeighbors()
    outputStr = ''
    for x in outlist:
        outputStr = outputStr + str(x) + " "
    print(outputStr)
    

if __name__== "__main__":
  main()