import sys
input = sys.stdin.readline
from collections import deque

def bfs(r,c):
    dq = deque([[r,c]])
    count = 1
    while dq:
        y, x = dq.popleft()
        visited[y][x] = True
        for move in moves:
            dy = y + moves[move][0]
            dx = x + moves[move][1]
            if 0 <= dy < N and 0 <= dx < N:
                if not visited[dy][dx] and gt[dy][dx] == '1':
                    dq.append([dy,dx])
                    visited[dy][dx] = True
                    count += 1
    return count
       
N = int(input())         
gt = []
visited = [[False for _ in range(N)] for _ in range(N)]
moves = {'up':(1,0),'right':(0,1),'down':(-1,0),'left':(0,-1)}
for _ in range(N):
    gt.append(input().strip())
answer = []
for r in range(N):    
    for c in range(N):
        if gt[r][c] == '1' and not visited[r][c]:
            answer.append(bfs(r,c))
if answer :
    answer.sort()
    print(len(answer))
    for i in answer:
        print(i)
else : print(0)