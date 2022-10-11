import sys
from collections import deque

def bfs(x,y):
    cnt = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dq = deque([[x,y]])
    
    while dq:
        x,y = dq.popleft()
        for i in range(4):
            nx = x+dx[i] 
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny< n:
                if gt[nx][ny] == 1: 
                    gt[nx][ny] = 0 
                    dq.append([nx,ny]) 
                    cnt += 1
    return cnt

# read
n = int(sys.stdin.readline())
gt = [[int(i) for i in sys.stdin.readline().strip()] for j in range(n)]
flag = [[0] * n for _ in range(n)]
ans = []

# main
for i in range(n):
    for j in range(n):
        if gt[i][j] == 1:
            gt[i][j] = 0
            ans.append(bfs(i,j))

# answer
ans.sort()
print(len(ans))
for i in ans:
    print(i)