# USED FOR BFS ALGORITHM https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

import os
import copy
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

        self.bfsList = []
        self.visited = []
        self.queue = []

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

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


    def bfsTest(self, visted, graph, node):

        self.visited.append(node)
        self.queue.append(node)

        currentColor = False

        self.colorMap[node] =  currentColor

        while self.queue:
            s = self.queue.pop(0)
            self.bfsList.append(s)
            #print (s, end = " ") 

            for neighbour in graph[s]:
                if neighbour not in self.visited:
                    self.colorMap[neighbour] = not self.colorMap.get(s)
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)


  
    def circuit(self, startNode):
        circuitLengths = []
        FirstDegreeAdjacencyList = self.graph.get(startNode)
        if len(FirstDegreeAdjacencyList) <= 1:
            return []
        traverseList = []
        # Get second degree list of nodes.
        for nodes in FirstDegreeAdjacencyList:
            for node2 in self.graph.get(nodes):
                if node2 not in traverseList and node2 != startNode:
                    traverseList.append(node2)
            #traverseList.extend(self.graph.get(startNode))
        
        alreadyTraversed = []
        circuitDistance = 2 # Starting at second degree nodes
        while traverseList != []:
            #print(startNode," ",circuitDistance, " : ", traverseList)
            #if startNode in traverseList:
            #    circuitLengths.append(circuitDistance)
            #    traverseList.remove(startNode)

            traverseListTemp = []

            for node in traverseList:
                if node == startNode:
                    circuitLengths.append(circuitDistance)
                    traverseList.remove(startNode)
                # Add nodes that were already traversed to list
                if node not in alreadyTraversed:
                    alreadyTraversed.append(node)


            for node in traverseList:
                # Get new list of nodes to traverse
                tempList = self.graph.get(node)
                for nodes in tempList:
                    if nodes not in alreadyTraversed:
                        traverseListTemp.append(nodes)

        
            traverseList.clear()
            traverseList = copy.deepcopy(traverseListTemp)

            circuitDistance = circuitDistance + 1
        return circuitLengths
        



    def isBiColorable(self):

        #self.bfsColorCheckTest(self.visited, self.graph, firstnode)
        #print(self.colorMap)
        for key in self.graph:
            for neighbor in self.graph.get(key):
                if self.colorMap.get(key) == self.colorMap.get(neighbor):
                    self.biColor = False
                    break


        #print(self.bfsList)
        #print(self.colorMap)

        #print(self.colorMap)
        
        #lengthOfCircuits = []

        #keyList = list(self.graph.keys())

        #for node in keyList:
        #    listr = self.circuit(node)
        #    for num in listr:
        #        if num % 2 != 0:
        #            self.biColor = False
        #            break

        #print(lengthOfCircuits)
        #for num in lengthOfCircuits:
        #    if num % 2 != 0:
        #        self.biColor = False
        #        break


    def deletionTraverse(self):
        graphCopy = copy.deepcopy(self.graph)

        # Start loopCount already accouting for nodes with no edges.
        loopCount = self.V - int(len(list(graphCopy.keys())))
        running = True
        alreadyTraversed = []
        TraverseList = graphCopy.get(list(graphCopy.keys())[0])
        graphCopy = self.removeNode(graphCopy, list(graphCopy.keys())[0])
        #print("Starting Node: ", list(graphCopy.keys())[0])
        
        if TraverseList is None:
            return -1
        while running:
            # print(TraverseList)

            if TraverseList == [] or TraverseList == None:
                for x in alreadyTraversed:
                    graphCopy = self.removeNode(graphCopy, x)
                alreadyTraversed.clear()
                loopCount = loopCount + 1
                self.circuitCount = 0
                #print(graphCopy)
                if graphCopy is None or graphCopy == {}:
                    return loopCount
                else:
                    TraverseList = graphCopy.get(list(graphCopy.keys())[0])
                    graphCopy = self.removeNode(graphCopy, list(graphCopy.keys())[0])

            newTraverseList = []

            for node1 in TraverseList:
                if graphCopy.get(node1) != None:
                    for x in graphCopy.get(node1):
                        if x not in alreadyTraversed:
                            newTraverseList.append(x)
                        elif self.circuitCount % 2 != 0:
                            self.biColor = False
                            return -1
                #graphCopy = self.removeNode(graphCopy, node1)

                    

                #print("LIST LENGTH: ", len(newTraverseList))
            self.circuitCount += 1
            alreadyTraversed.extend(TraverseList)
            TraverseList.clear()
            TraverseList = newTraverseList.copy()
            newTraverseList.clear()
        # print("THIS")
        return -1

    """
    def bfsResults(self):
        output = ""
        for x in range(self.V):
            output += str(self.getTraverseLength(str(1), str(x + 1))) + " "
        #print(output)
        return output

    # Distance to get from u to v
    def getTraverseLength(self, u, v):
        #print(u , v)
        #print(self.graph)
        possibleToTraverseToV = False
        canExitU = False
        #for x in self.graph:
        #    if u in self.graph[x]:
        #        canExitU = True
        #if not canExitU:
        #    return -1
        if u == v:
            return 0
        else:
            loopCount = 0
            running = True
            TraverseList = self.graph.get(u).copy()
            alreadyTraversed = []
            #print("Current Destination:", v, " ", TraverseList)
            if TraverseList is None:
                return -1
            while running:
                #print(TraverseList)
                if TraverseList == [] or TraverseList == None:
                    running = False
                    break
                newTraverseList = []
                if v in TraverseList:
                    return (loopCount + 1)
                else:
                    for node1 in TraverseList:
                        if self.graph.get(node1) != None:
                            for x in self.graph.get(node1):
                                if x not in alreadyTraversed:
                                    newTraverseList.append(x)

                    #print("LIST LENGTH: ", len(newTraverseList))        

                    

                alreadyTraversed.extend(TraverseList)
                TraverseList.clear()
                TraverseList = newTraverseList.copy()
                newTraverseList.clear()
                loopCount = loopCount + 1
            #print("THIS")
            return -1

    """

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
    """
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    graphs = []
    graphEdges = []
    numOfVerticies = 0
    numOfEdges = 0
    firstVals = True
    for x in numInput:
    """
    listOfMaps = []

    while True:
        numOfStarsOnMap = input('')
        if int(numOfStarsOnMap) == 0:
            break
        numOfLines = input('')
        if int(numOfLines) == 0:
            listOfMaps.append([])
        else:
            list1 = []
            list1.append(numOfStarsOnMap)
            for i in range(int(numOfLines)):
                list1.append([str(item) for item in input('').split()])
            listOfMaps.append(list1)

    test = []
    for graphs in listOfMaps:
        temp = graphs
        g = Graph(int(graphs[0]))
        for x in range(1, len(temp)):
            val1 = (temp[x])[0]
            val2 = (temp[x])[1]
            g.addEdge(val1, val2)
        if (g.V == 1):
            print("BICOLORABLE")
        else:
            #g.isBiColorable()
            keyList = list(g.graph.keys())
            #if len(keyList) <= 2:
            #    print("BICOLORABLE")
            #    continue
            firstnode = keyList[0]
            g.bfsTest(g.visited, g.graph, firstnode)
            #print(g.bfsList)
            #print(g.colorMap)
            g.isBiColorable()
            if(g.biColor):
                print("BICOLORABLE")
            else:
                print("NOT BICOLORABLE") 



    """
    g = Graph(int(numOfVerticies))
    for x in graphEdges:
        #print(x[0], x[1])
        g.addEdge(x[0], x[1])

    # g.printGraph2()
    # print(g.V)
    x1 = g.deletionTraverse()

    if g.biColor:
        print("BICOLORABLE")
    else:
        print("NOT BICOLORABLE")

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(x1))
    """

if __name__ == "__main__":
    main()
