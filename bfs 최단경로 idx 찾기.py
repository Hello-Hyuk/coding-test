from collections import deque
import copy

moves = {1:(0,1),2:(1,0),3:(0,-1),4:(-1,0)}

def bfs():
    dq = deque([[0,0,[]]])
    while dq:
        r, c, route = dq.popleft()
        route.append([r, c])
        visited[r][c] = True
        if [r, c] == [3,3]:
            return route
        for move in moves:
            dr = (r + moves[move][0]) % N
            dc = (c + moves[move][1]) % M
            if not visited[dr][dc] and board[dr][dc] > 0:
                dq.append([dr,dc,copy.deepcopy(route)])
    return -1

def bfs2():
    dq = deque([[0,0,[]]])
    while dq:
        r, c, route = dq.popleft()
        visited2[r][c] = True
        if [r, c] == [3,3]:
            return route
        for move in moves:
            dr = (r + moves[move][0]) % N
            dc = (c + moves[move][1]) % M
            if not visited2[dr][dc] and board[dr][dc] > 0:
                route.append([dr, dc])
                dq.append([dr,dc,copy.deepcopy(route)])
                route.pop()
    return -1

N = 4 
M = 5
board = [[1 for _ in range(M)] for _ in range(N)]
board[0][4] = 0
visited = [[False for _ in range(M)] for _ in range(N)]
visited2 = [[False for _ in range(M)] for _ in range(N)]

print(bfs())
print(bfs2())
