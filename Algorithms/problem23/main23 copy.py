import sys
import os

class directed_graph:
    def __init__(self):
        self.nodes = {}

    class node:
        def __init__(self, label):
            self.label = label
            self.edge_tuples = []

    def add_node(self, label):
        node = self.node(label)
        self.nodes[label] = node

    def construct_graph(self, n, edge_list):
        # add a dummy "source_node" to our graph and add an edge from source to every node with weight 0
        self.add_node(-1)
        for i in range(1, n + 1):
            self.add_node(i)
            self.nodes[-1].edge_tuples.append((self.nodes[i], 0))

        for edge in edge_list:
            self.nodes[edge[0]].edge_tuples.append((self.nodes[edge[1]], edge[2]))

    def has_negative_cycle(self, source=-1):
        distances = {}
        for v in self.nodes:
            distances[v] = float("Inf")
        distances[source] = 0

        for _ in range(len(self.nodes) - 1):
            for u in self.nodes:
                if distances[u] != float("Inf"):
                    for v, weight in self.nodes[u].edge_tuples:
                        new_len = distances[u] + weight
                        if distances[v.label] > new_len:
                            distances[v.label] = new_len

        for u in self.nodes:
            if distances[u] != float("Inf"):
                for v, weight in self.nodes[u].edge_tuples:
                    if distances[v.label] > distances[u] + weight:
                        return "1"
        return "-1"


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
                nodes = int(x)
                #g = Graph(int(x))
                firstLineInput = False
            else:
                edges.append([int(x[0]), int(x[1]), int(x[2])])
        g = directed_graph()
        g.construct_graph(nodes, edges)
        tempOut += str(g.has_negative_cycle()) + " "
    
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

'''
if __name__ == "__main__":
    
    Given: A positive integer k≤20 and k simple directed graphs with integer edge weights from −103 to 103 and n≤103 
    vertices in the edge list format.
    Return: For each graph, output "1" if it contains a negative weight cycle and "-1" otherwise.
    
    input_lines = sys.stdin.read().splitlines()
    k = int(input_lines[0])

    i = 1
    n_vert_list = []
    edge_lists = []
    while i < len(input_lines):
        num_vertices, num_edges = [int(x) for x in input_lines[i].split()]
        n_vert_list.append(num_vertices)
        edge_lists.append([[int(x) for x in line.split()] for line in input_lines[i + 1: i + 1 + num_edges]])
        i = i + 1 + num_edges

    result = []
    for num_vertices, edge_list in zip(n_vert_list, edge_lists):
        G = directed_graph()
        G.construct_graph(num_vertices, edge_list)
        result.append(G.has_negative_cycle())
    print(" ".join(result))

'''