import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
K = int(input())
def dfs(idx,num):
    global answer
    visited[idx] = True
    for i in adj[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i,num+1)
            answer += 1

adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = 0

for _ in range(K):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    
dfs(1,0)
print(answer)