import sys
from collections import deque
input = sys.stdin.readline

def bfs(r,c,step):
    dq = deque([[r,c,step]])
    min_step = I**2
    while dq:
        y, x, s = dq.popleft()
        if y == gr and x == gc:
            min_step = min(min_step,s)
        for move in moves:
            dy = y + moves[move][0]
            dx = x + moves[move][1]
            if 0 <= dy < I and 0 <= dx < I:
                if not visited[dy][dx] :
                    visited[dy][dx] = True
                    dq.append([dy,dx,s+1])
    return min_step

K = int(input())
moves = {1:(-2,-1),2:(-2,1),3:(-1,-2),4:(-1,2),5:(2,-1),6:(2,1),7:(1,-2),8:(1,2)}
for _ in range(K):
    I = int(input())
    visited = [[False for _ in range(I)] for _ in range(I)]
    r, c = map(int, input().split())
    gr, gc = map(int, input().split())
    print(bfs(r,c,0))
    