import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = 1
    for e in adj[v]:
        if visited[e] == -1:
            dfs(e)
            
n, m = map(int, sys.stdin.readline().split())
# 간선 리스트
adj = [[0] for _ in range(n + 1)]
visited = [-1] * (n + 1)
print(adj, visited)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)
    
for i in adj:
    i.sort()
    
count = 0
for j in range(1, n + 1):
    if visited[j] == -1:
        dfs(j)
        count += 1

print(count)