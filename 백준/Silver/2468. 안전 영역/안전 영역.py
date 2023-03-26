import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,r,min_h,visited):
    moves = {'up':(-1,0),'right':(0,1),'down':(1,0),'left':(0,-1)}
    dq = deque([(i,r)])
    while dq:
        y, x = dq.popleft()
        visited[y][x] = True
        for move in moves:
            dy = y + moves[move][0]
            dx = x + moves[move][1]
            if 0 <= dy < N and 0 <= dx < N and areas[dy][dx] > min_h:
                if not visited[dy][dx]:
                    dq.append([dy,dx])
                    visited[dy][dx] = True
    return visited

N = int(input())
areas = []
min_h = 100
max_h = 0
for _ in range(N):
    area = list(map(int, input().split()))
    min_h = min(min(area),min_h)  
    max_h = max(max(area),max_h)
    areas.append(area)

ans = []
min_h = max(0,min_h-1)
while 1:
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for r in range(N):
            if areas[i][r] > min_h and not visited[i][r]:
                visited = bfs(i,r,min_h,visited)    
                cnt += 1
            else : 
                visited[i][r] = True
    ans.append(cnt)
    if min_h == max_h:
        break
    min_h += 1

print(max(ans))
            