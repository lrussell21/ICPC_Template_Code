
max = 202

cap = [[] * max] * max
passed = [[] * max] * max
adj = [[]] * max
par = [-1] * max
source = None
sink = None

def bfs():
    global cap
    global passed
    global adj
    global par
    global source
    global sink
    # Init par to all -1's
    par = [-1] * max
    par[source] = -5
    queue = []
    queue.append(source)
    while queue != []:
        # u is front of queue. That item is removed from queue
        u = queue.pop(len(queue) - 1)
        for i in range(len(adj[u])):
            v = adj[u][i]
            if par[v] == -1 and (cap[u][v] - passed[u][v]) > 0:
                par[v] = u
                if v == sink:
                    return True
                queue.append(v)

    return False

# Used maxflow algorithm adapted from here https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
def getMaxFlow():
    global cap
    global passed
    global adj
    global par
    global source
    global sink

    maxflow = 0
    flow = None
    # While bfs is still finding max flow
    while(bfs()):
        now = sink
        flow = 1000000
        while(now != source):
            prev = par[now]
            flow = min(flow, cap[prev][now] - passed[prev][now])
            now = prev
        maxflow += flow
        now = sink
        while(now != source):
            prev = par[now]
            passed[prev][now] += flow
            passed[now][prev] -= flow
            now = prev
    return maxflow

amountOfProblems = int(input())
chambers = None
for _ in range(amountOfProblems):
    chambers = int(input())
    #Init adj, cap, passed for problem
    adj = [None] * max
    cap = [None] * max
    passed = [None] * max
    for ind in range(max):
        adj[ind] = []
        cap[ind] = [0] * max
        passed[ind] = [0] * max
    source = 1
    sink = chambers
    for i in range(1, chambers):
        #print("i----", i)
        temp = input()
        temp = temp.strip().split()
        temp = list(map(int, temp))
        for num in temp[1:]:
            if i != 1 and num != chambers:
                cap[i][num] = 10000000
            else:
                cap[i][num] = 1
            adj[i].append(num)
            adj[num].append(i)
    print(getMaxFlow())
    # There is a newline between problems or else NZEC
    input()

