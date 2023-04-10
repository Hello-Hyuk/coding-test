import sys
input = sys.stdin.readline
from collections import deque

def bfs(n,m,_cnt):
    dq = deque([[n,m,_cnt]])
    while dq:
        r,c,cnt = dq.popleft()
        if r == N-1 and c == M-1:
            print(cnt)
            return 
        visited[r][c] = True
        for move in moves:
            nr = r + moves[move][0]
            nc = c + moves[move][1]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and gt[nr][nc] == '1':
                dq.append([nr,nc,cnt+1])
                visited[nr][nc] = True
    
N, M = map(int,input().split())
gt = []
for _ in range(N):
    gt.append(list(map(str,input().strip())))
moves = {'up':(-1,0),'right':(0,1),'down':(1,0),'left':(0,-1)}
visited = [[False for _ in range(M)] for _ in range(N)]
bfs(0,0,1)