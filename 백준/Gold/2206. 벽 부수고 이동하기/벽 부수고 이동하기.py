import sys
from collections import deque
input = sys.stdin.readline

def bfs(r,c,br):
    dq = deque([[r,c,br]])
    visited[r][c][0] = 1
    while dq:
        y, x, b = dq.popleft()
        if y == N-1 and x == M-1:
            return visited[y][x][b]
        for move in moves:
            dy = y + moves[move][0]
            dx = x + moves[move][1]
            if 0 <= dy < N and 0 <= dx < M and not visited[dy][dx][b]:
                    if gt[dy][dx] == '0':
                        visited[dy][dx][b] = visited[y][x][b]+1
                        dq.append([dy,dx,b])
                    elif gt[dy][dx] == '1':
                        if not b :
                            visited[dy][dx][1] = visited[y][x][b]+1
                            dq.append([dy,dx,True])
    return -1
        
moves = {1:(-1,0),2:(0,1),3:(1,0),4:(0,-1)}
N, M = map(int,input().split())
gt = []
for _ in range(N):
    gt.append(str(input().strip()))
visited = [[[0]*2 for _ in range(M)]for _ in range(N)]
print(bfs(0,0,False))



'''
3 3
001
111
000

2 4
0111
0010


'''