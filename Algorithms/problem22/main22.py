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


    # function to add an edge to graph
    def addEdge(self, u, v, weight):
        self.graph[int(u)].append([int(v), int(weight)])
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

      
    def BellmanFord(self, start):  
  
        # Create distance list
        dist = [float("Inf")] * (self.V + 1)
        dist[start] = 0 # Starting node will be of length 0
  
        # Repeat main algorithm for each verticy
        for index in range(self.V - 1):  
            # Goes through all the verticies and checks if the parent verticy and its weight to the next verticy is less than infinity.
            # In the end we get the least distance because the parent for loop itterates through all the verticies. So each one is checked more than once.
            for u in self.graph:
                temp = self.graph.get(u)
                for x in temp:
                    v = x[0]
                    weight = x[1]
                    if dist[u] != float("Inf") and int(dist[u]) + weight < dist[v]:
                        dist[v] = int(dist[u]) + weight

        # Print answer
        outputText = ''
        for i in range(1, self.V + 1):
            if(dist[i] == float("Inf")):
                outputText += "x" + " "
                pass
            else:
                outputText += str(dist[i]) + " "
        print(outputText)
        return outputText



def main():
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    listOfArrays = []
    verticies = 0
    firstLineSkip = True
    for x in numInput:
        
        if firstLineSkip:
            temp1 = x
            temp1 = temp1.split()
            print(temp1[0])
            verticies = int(temp1[0])
            firstLineSkip = False
            continue
        temp = x.strip().split()
        temp = list(map(int, temp))
        listOfArrays.append(temp)

    print(verticies)

    g = Graph(verticies)
    for x in listOfArrays:
        g.addEdge(x[0], x[1], x[2])
    
    #g.printGraph()
    x1 = g.BellmanFord(1)

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(x1))


if __name__== "__main__":
  main()