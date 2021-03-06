import os
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.output = ''
        self.count = 0

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

    def deletionTraverse(self):
        graphCopy = self.graph.copy()


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
                #graphCopy = self.removeNode(graphCopy, node1)

                    

                #print("LIST LENGTH: ", len(newTraverseList))

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
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    graphEdges = []
    numOfVerticies = 0
    firstVals = True
    for x in numInput:
        if firstVals:
            numOfVerticies = x.split()[0]
            firstVals = False
        else:
            graphEdges.append(x.split())

    g = Graph(int(numOfVerticies))
    for x in graphEdges:
        #print(x[0], x[1])
        g.addEdge(x[0], x[1])

    # g.printGraph2()
    # print(g.V)
    x1 = g.deletionTraverse()

    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(x1))


if __name__ == "__main__":
    main()
