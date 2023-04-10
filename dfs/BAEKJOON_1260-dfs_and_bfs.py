import sys
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,1]
def dfs(v):
    dfs_visited[v] = 1
    print(v, end=" ")
    for i in adj[v]:
        if dfs_visited[i] == -1:
            dfs(i)

def bfs(v):
    dq = deque([v])
    bfs_visited[v] = 1
    while dq:
        v = dq.popleft()
        print(v, end=" ")
        for i in adj[v]:
            if bfs_visited[i] == -1:
                bfs_visited[i] = 1
                dq.append(i)
            
n, m, v = map(int,(sys.stdin.readline().split()))
dfs_visited = [-1] *(n+1)
bfs_visited = [-1] *(n+1)
adj = [[] for _ in range(n+1)]
print(adj)
# graph
#graph = [[0] * (n + 1) for _ in range(n + 1)] 

for _ in range(m):
    j, k = map(int,(sys.stdin.readline().split()))
    adj[j].append(k)
    adj[k].append(j)

for i in adj:
    i.sort()
    
dfs(v)
print()
bfs(v)