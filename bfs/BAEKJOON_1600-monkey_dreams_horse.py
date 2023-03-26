import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

h_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
h_dy = [-2, -1, 1, 2, 2, 1, -1, -2]
import sys
sys.setrecursionlimit(10**6)
def bfs():
    dq = deque([[0,0]])
def bfs():
    # y, x, cnt, k 
    dq = deque([[0,0,0,k]])
    while dq :
        y, x, cnt, curr_k = dq.popleft()
        if curr_k > 0:
            for i in range(len(h_dx)):
                nx = x+h_dx[i]
                ny = y+h_dy[i]
                if 0<=nx<m and 0<=ny<n and world[ny][nx] == 0:                
                    if visited[ny][nx][0] == -1 or visited[ny][nx][1] < curr_k-1:
                        if ny == n-1 and nx == m-1:
                            return cnt + 1
                        visited[ny][nx][0] = 1
                        visited[ny][nx][1] = curr_k-1
                        dq.append([ny,nx,cnt+1,curr_k-1])
        for i in range(len(dx)):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<m and 0<=ny<n and world[ny][nx] == 0:
                    if visited[ny][nx][0] == -1 or visited[ny][nx][1] < curr_k:
                        if ny == n-1 and nx == m-1:
                            return cnt + 1
                        visited[ny][nx][0] = 1
                        visited[ny][nx][1] = curr_k
                        dq.append([ny,nx,cnt+1,curr_k])
    return -1    
                             
k = int(sys.stdin.readline())
m , n = map(int,(sys.stdin.readline().split()))

world = []
for _ in range(n):
    world.append(list(map(int,(sys.stdin.readline().split()))))

visited = [[[-1 for _ in range(2)] for _ in range(m)] for _ in range(n)]

if n == 1 and m == 1:
    print(0)    
else : 
    print(bfs())