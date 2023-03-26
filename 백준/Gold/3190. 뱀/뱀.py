import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples, snake_cmd_time, snake_cmd_dir = [], [], deque([])
for _ in range(K):
    apples.append(list(map(int,input().split())))
    
L = int(input())

for _ in range(L):
    time, dir = input().split()
    snake_cmd_time.append(int(time))
    snake_cmd_dir.append(str(dir))
    
cmds = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
cmd_idx = 0
cmd_count = 1

board = [[0 for _ in range(N+2)] for _ in range(N+2)]
for i in range(N+2):
    for j in range(N+2):
        if i == 0 or j == 0 or i == N+1 or j == N+1:
            board[i][j] = -1
    
snake_idx = deque([[1,1]])
time = 0

while 1:
    s_idx = snake_idx[-1]
    if time in snake_cmd_time:
        n_dir = snake_cmd_dir.popleft()
        if n_dir == 'D':    
            cmd_idx += 1
            cmd_idx %= 4
        elif n_dir == 'L': 
            cmd_idx -= 1
            if cmd_idx == -1:
                cmd_idx = 3    
    ny = s_idx[0] + cmds[cmd_idx][0]
    nx = s_idx[1] + cmds[cmd_idx][1]
    if board[ny][nx] == -1:
        break
    flag = False
    for apple in apples:
        if [ny,nx] == apple:
            apples.remove(apple)
            flag = True
    if [ny,nx] in snake_idx:
        break
    snake_idx.append([ny,nx])
    if not flag :
        snake_idx.popleft()
    time += 1

print(time+1)