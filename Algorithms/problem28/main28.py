import os
from collections import defaultdict
# Used Tarjan's algorithm mentioned in class.
# Got it from here https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

class Graph: 
   
    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices  
          
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
          
        self.Time = 0
        self.outputnums = []

        self.scc = 0
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
          

    def tarjansUtil(self,u, low, disc, stackMember, st): 
  
        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
        stackMember[u] = True
        st.append(u) 
  
        # Go through all vertices adjacent to this 
        for v in self.graph[u]: 
              
            # If v is not visited yet, then recur for it 
            if disc[v] == -1 : 
              
                self.tarjansUtil(v, low, disc, stackMember, st) 
  
                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                # Case 1 (per above discussion on Disc and Low value) 
                low[u] = min(low[u], low[v]) 
                          
            elif stackMember[v] == True:  
  
                '''Update low value of 'u' only if 'v' is still in stack 
                (i.e. it's a back edge, not cross edge). 
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v]) 
  
        outputNums = []
        # head node found, pop the stack and print an SCC 
        w = -1 #To store stack extracted vertices
        if low[u] == disc[u]: 
            while w != u: 
                w = st.pop() 
                self.outputnums.append(w)
                stackMember[w] = False
            self.scc += 1
            
                  
              
      
  
    def tarjans(self): 
   
        # Mark all the vertices as not visited  
        # and Initialize parent and visited,  
        # and ap(articulation point) arrays 
        disc = [-1] * (self.V + 1) 
        low = [-1] * (self.V + 1) 
        stackMember = [False] * (self.V + 1) 
        st =[] 
          
  
        # Call the recursive helper function  
        # to find articulation points 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if disc[i] == -1: 
                self.tarjansUtil(i, low, disc, stackMember, st) 


def main():
    filename = "/input.txt"
    dir_path = os.path.dirname(__file__)
    f = open(str(dir_path) + filename)
    numInput = f.readlines()
    nodes = 0
    listOfArrays = []
    firstLineSkip = True
    for x in numInput:
        if firstLineSkip:
            nodes = x.strip().split()
            nodes = int(nodes[0])
            print(nodes)
            firstLineSkip = False
            continue
        listOfArrays.append(list(map(int,x.strip().split())))
    print(listOfArrays)
    
    g = Graph(nodes)
    for edge in listOfArrays:
        g.addEdge(edge[0], edge[1])

    g.tarjans()
    print(g.scc - 1)

    
    # File Output
    filename = "/output.txt"
    dir_path = os.path.dirname(__file__)
    filewrite = open(str(dir_path) + filename, 'w')
    filewrite.write(str(g.scc - 1))


if __name__== "__main__":
  main()