import sys
input = sys.stdin.readline
from collections import deque
# 적록색맹 R+G, B
# 정상 R, G, B
def bfs(r,c,color):
    dq = deque([[r,c]])
    while dq:
        y, x = dq.popleft()
        visited[y][x] = True
        for move in moves:
            ny = y + moves[move][0]
            nx = x + moves[move][1]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if gt[ny][nx] == color:
                    visited[ny][nx] = True
                    dq.append([ny,nx])

    return 1

N = int(input())
gt = []
moves = {1:(1,0),2:(0,1),3:(-1,0),4:(0,-1)}
for _ in range(N):
    gt.append(list(input().rstrip()))
visited = [[False for _ in range(N)] for _ in range(N)]
ans = 0
ans2 = 0
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            ans += bfs(r,c,gt[r][c])

for r in range(N):
    for c in range(N):
        if gt[r][c] == 'R':
            gt[r][c] = 'G'
            
visited = [[False for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            ans2 += bfs(r,c,gt[r][c])

print(ans,ans2)