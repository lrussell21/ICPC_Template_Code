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
        for _ in range(self.V - 1):  
            # Goes through all the verticies and checks if the parent verticy and its weight to the next verticy is less than infinity.
            # In the end we get the least distance because the parent for loop itterates through all the verticies. So each one is checked more than once.
            for u in self.graph:
                if dist[u] != float("Inf"):
                    for x in self.graph.get(u):
                        v = x[0]
                        weight = x[1]
                        if (int(dist[u]) + weight) < dist[v]:
                            dist[v] = int(dist[u]) + weight

        print(dist)
        # If there is a shorter path it means there is a negative weight cycle

        for u in self.graph:
            if dist[u] != float("Inf"):
                for x in self.graph.get(u):
                    v = x[0]
                    weight = x[1]
                    if (int(dist[u]) + weight) < dist[v]:
                        print("Graph contains negative weight cycle")
                        return 1

                        #return 1
        
        # Gets through negative cycle check
        return -1




def main():
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    
    numOfProblems = 0

    listOfProblems = []

    tempList = []

    verticies = 0

    verticiesToInput = 0

    firstLineSkip = True
    startNewProblemInput = True
    skipBlank = False
    for x in numInput:
        # Get number of problems and get ready for input of problems
        if skipBlank:
            skipBlank = False
            continue
        if firstLineSkip:
            numOfProblems = int(x)
            firstLineSkip = False
            skipBlank = True
            continue
        if startNewProblemInput:
            temp = x.split()
            verticies = int(temp[0])
            verticiesToInput = int(temp[1])
            tempList.append(verticies)
            startNewProblemInput = False
            continue
        if verticiesToInput > 0:
            temp = x.split()
            tempList.append([int(temp[0]), int(temp[1]), int(temp[2])])
            verticiesToInput -= 1
            continue
        else:
            #startNewProblemInput = True
            # Push problem into array and start over
            listOfProblems.append(tempList[:])
            tempList.clear()

            # Input for new problem 
            temp = x.split()
            #print(temp)
            verticies = int(temp[0])
            verticiesToInput = int(temp[1])
            tempList.append(verticies)
            continue
    listOfProblems.append(tempList)


    #print(listOfProblems)
    tempOut = ''
    firstLineInput = True
    for problem in listOfProblems:
        firstLineInput = True
        print("New problem")
        for x in problem:
            if firstLineInput:
                g = Graph(int(x))
                firstLineInput = False
            else:
                g.addEdge(int(x[0]), int(x[1]), int(x[2]))
        tempOut += str(g.BellmanFord(-1)) + " "
    
    #g.printGraph()
    #g.BellmanFord(1)
    print(tempOut)
    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(tempOut))


if __name__== "__main__":
  main()