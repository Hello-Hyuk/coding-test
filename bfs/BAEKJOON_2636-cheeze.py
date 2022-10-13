import sys
from collections import deque

def bfs():
    cnt = 0
    flag = [[0] * n for _ in range(m)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dq = deque([[0,0]])
    flag[0][0] = 1
    
    while dq:
        y,x = dq.popleft()
        for i in range(4):
            nx = x+dx[i] 
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and flag[ny][nx] == 0:
                if gt[ny][nx] == 0: 
                    flag[ny][nx] = 1 
                    dq.append([ny,nx])
                else : 
                    gt[ny][nx] = 0 
                    flag[ny][nx] = 1
                    cnt += 1
    ans.append(cnt)
    return cnt

# read
m , n = map(int,(sys.stdin.readline().split()))
gt = []
for _ in range(m):
    gt.append(list(map(int,(sys.stdin.readline().split()))))
ans = []

# main
t = 0
while True:
    cnt = bfs()
    if cnt == 0:
        break
    t += 1

# answer
print(t)
print(ans[-2])