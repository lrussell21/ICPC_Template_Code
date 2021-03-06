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
        self.containsCycleBool = False

        self.bfsList = []
        self.visited = []
        self.queue = []

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
                else:
                    self.containsCycleBool = True


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
            if startNode in traverseList:
                circuitLengths.append(circuitDistance)
                traverseList.remove(startNode)
                self.containsCycleBool = True
                return

            traverseListTemp = []


            for node in traverseList:
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
        



    def containsCycle(self):
        keyList = list(self.graph.keys())
        self.bfsTest(self.visited, self.graph, keyList[0])

        #keyList = list(self.graph.keys())

        #for node in keyList:
        #    if not self.containsCycleBool:
        #        lengthOfCircuits.extend(self.circuit(node))


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
    graphs = []
    graphEdges = []
    numOfVerticies = 0
    skipFirstLine = True
    firstVals = True
    for x in numInput:
        if skipFirstLine:
            skipFirstLine = False
            continue
        vals = x.split()
        if vals == []:
            firstVals = True
            if graphEdges != []:
                graphs.append(copy.deepcopy(graphEdges))
                graphEdges.clear()
            continue
        if firstVals:
            numOfVerticies = vals[0]
            graphEdges.append(numOfVerticies)
            firstVals = False
        else:
            graphEdges.append(vals)

    # Get last graph because there isn't a "\n" at end of file
    graphs.append(copy.deepcopy(graphEdges))

    #for gr in graphs:
    #    print(gr)


    """
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
    """

    test = []
    for gr in graphs:
        temp = gr
        g = Graph(int(gr[0]))
        for x in range(1, len(temp)):
            val1 = (temp[x])[0]
            val2 = (temp[x])[1]
            g.addEdge(val1, val2)
        #g.printGraph()
        if (g.V == 1 or 0):
            print("1")

        else:
            g.containsCycle()
            if(g.containsCycleBool):
                print("-1")
            else:
                print("1") 



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
