import sys
from collections import deque
input = sys.stdin.readline
'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
'''
N, M = map(int, input().split()) 

gt = []
for _ in range(N):
    gt.append(list(map(int,input().split())))


moves = {'up':(-1,0),'down':(1,0),'right':(0,1),'left':(0,-1)}

def bfs(n,m):
    dq = deque([[n,m]])
    visited[n][m] = True
    melt = [[0 for _ in range(M)]for _ in range(N)]
    while dq:
        y, x = dq.popleft()
        for move in moves:
            nx = x+moves[move][1]
            ny = y+moves[move][0]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if gt[ny][nx] == 0:
                    melt[y][x] += 1
                if gt[ny][nx] != 0:
                    dq.append([ny,nx])
                    visited[ny][nx] = True      
    for n in range(N):
        for m in range(M):
            gt[n][m] -= melt[n][m]
            if gt[n][m] < 0 : gt[n][m] = 0 
    #for r in gt:
        #print(*r)
    #for v in visited:
        #print(*v)
flag = True
year = 0
while 1:
    cnt = 0
    #print("round - ",year)
    visited = [[False for _ in range(M)]for _ in range(N)]
    cnt_z = 0
    for n in range(N):
        for m in range(M):
            if gt[n][m] != 0 and not visited[n][m]:
                #print("bfs")
                bfs(n,m)
                cnt += 1
            if gt[n][m] == 0:
                cnt_z += 1
    if cnt >= 2:
        flag = False
        print(year)
        break
    if cnt_z == N*M:
        print(0)
        break
    year += 1

