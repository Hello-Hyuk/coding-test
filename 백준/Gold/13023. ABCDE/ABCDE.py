import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(idx,cnt):
    if cnt == 4:
        print(1)
        exit()
    for i in friend[idx]:
        if not visited[i]:
            visited[idx] = True
            dfs(i,cnt+1)
            visited[idx] = False
            
            
N, M = map(int, input().split())
friend = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i,0) 
    visited[i] = False

print(0)