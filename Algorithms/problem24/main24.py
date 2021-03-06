import os
import copy
import sys
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        #self.graph = []
        self.alreadyVisted = [False] * self.V
        self.output = ''
        self.count = 0
        self.circuitCount = 0


    # function to add an edge to graph
    def addEdge(self, u, v, weight):
        #self.graph.append([u, v, weight])
        self.graph[u][v] = weight
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

    def minDistance(self, dist, sett):
        minTemp = float("inf")
        minIndex = 0    
        for v in range(self.V):
            if dist[v] < minTemp and sett[v] == False:
                minTemp = dist[v]
                minIndex = v
        
        return minIndex
    
    def deletemin(self, queue):
        tempMin = float("inf")
        index = -1
        for weight in queue:
            for node in self.graph:
                if node[2] < tempMin:
                    pass
            

    def dijkstras(self, s):

        dist = [float("inf")] * self.V
        dist[s] = 0
        sett = [False] * self.V

        for _ in range(self.V):

            u = self.minDistance(dist, sett)

            sett[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sett[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        
        output = ''
        for node in range(self.V):
            if dist[node] == float("inf"):
                output += "-1 "
            else:
                output += str(dist[node]) + " "
        return output

def main():
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    tempList = []
    verticies = 0
    firstLineSkip = True
    for x in numInput:
        # Get number of problems and get ready for input of problems
        if firstLineSkip:
            verticies = int(x.split()[0])
            firstLineSkip = False
            continue
        temp = x.split()
        tempList.append([int(temp[0]), int(temp[1]), int(temp[2])])



    g = Graph(verticies)
    for edge in tempList:
        g.addEdge((edge[0] - 1), (edge[1] - 1), edge[2])

    tempOut = g.dijkstras(0)
    print(tempOut)

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(tempOut))


if __name__== "__main__":
  main()