# import sys 
# from math import inf
# sys.setrecursionlimit(10**6)

# def dfs(start, next, cost, visited):
#     global ans 
#     if len(visited) == n:
#         if gt[next][start] != 0:
#             ans = min(ans, cost + gt[next][start])
#         return

#     for i in range(n):
#         if i not in visited and gt[next][i] != 0 and i != start:
#             visited.append(i)
#             dfs(start, i, cost + gt[next][i], visited)
#             visited.pop()

# n = int(sys.stdin.readline())
# gt = []
# for _ in range(n):
#     gt.append(list(map(int,sys.stdin.readline().split())))

# ans = inf
# for v in range(n):
#     dfs(v,v,0,[v])
# print(ans)
    
# 하나 잡고 순회
import sys 
from math import inf
sys.setrecursionlimit(10**6)

def dfs(curr, cost, cnt):
    global ans 
    if cnt == n:
        if gt[curr][0] != 0:
            ans = min(ans, cost + gt[curr][0])
        return

    for i in range(n):
        if visited[i]==False and gt[curr][i] != 0:
            visited[i] = True
            dfs(i, cost + gt[curr][i], cnt+1)
            visited[i] = False

n = int(sys.stdin.readline())
gt = []
for _ in range(n):
    gt.append(list(map(int,sys.stdin.readline().split())))
visited = [False] * n
ans = inf

visited[0] = True
dfs(0,0,1)

print(ans)
    
        