import os


class Graph:  
  
    def __init__(self, vertices):  
        self.V = vertices # No. of vertices  
        self.graph = []  
  
    # function to add an edge to graph  
    def addEdge(self, u, v, w):  
        self.graph.append([u, v, w])  
          
    # utility function used to print the solution  
    def printArr(self, dist):  
        print("Vertex Distance from Source")  
        for i in range(self.V):  
            print("{0}\t\t{1}".format(i, dist[i]))  
      
    # The main function that finds shortest distances from src to  
    # all other vertices using Bellman-Ford algorithm. The function  
    # also detects negative weight cycle  
    def BellmanFord(self, src):  
  
        # Step 1: Initialize distances from src to all other vertices  
        # as INFINITE

        dist = [float("Inf")] * (self.V + 1)
        dist[src] = 0
  
  
        # Step 2: Relax all edges |V| - 1 times. A simple shortest  
        # path from src to any other vertex can have at-most |V| - 1  
        # edges  
        for _ in range(self.V - 1):  
            # Update dist value and parent index of the adjacent vertices of  
            # the picked vertex. Consider only those vertices which are still in  
            # queue  
            for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        dist[v] = dist[u] + w  
  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
  
        for u, v, w in self.graph:  
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        print("Graph contains negative weight cycle") 
                        return 1
                          
        # print all distance
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
    nodes = 0
    edges = []
    for problem in listOfProblems:
        firstLineInput = True
        print("New problem")
        edges.clear()
        for x in problem:
            if firstLineInput:
                g = Graph(int(x))
                #g = Graph(int(x))
                firstLineInput = False
            else:
                g.addEdge(int(x[0]), int(x[1]), int(x[2]))
        tempOut += str(g.BellmanFord(0)) + " "
    
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
