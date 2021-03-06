# Python3 program to print DFS traversal  
# from a given given graph 
from collections import defaultdict 
  
# This class represents a directed graph using 
# adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def topologicalSort(self, v, visited): 
  
        # Mark the current node as visited  
        # and print it 
        visited[v] = True
        print(v, end = ' ') 
  
        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  

    def topologicalsortStart(self, v): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (max(self.graph)+1) 
  
        # Call the recursive helper function  
        # to print DFS traversal 
        self.topologicalSort(v, visited) 
  
# Driver code 
  
# Create a graph given  
# in the above diagram 
g = Graph() 
g.addEdge(1, 2) 
g.addEdge(3, 1) 
g.addEdge(3, 2) 
g.addEdge(4, 3) 
g.addEdge(4, 2) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(1)
  
# This code is contributed by Neelam Yadav 