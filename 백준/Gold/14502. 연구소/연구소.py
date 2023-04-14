import sys
input = sys.stdin.readline
from collections import deque
import copy
from itertools import combinations

def bfs(v_idx):
    visited = [[False for _ in range(M)] for _ in range(N)]
    tmp_gt = copy.deepcopy(gt)
    dq = deque(v_idx)
    cnt = 0
    while dq:
        y, x = dq.popleft()
        visited[y][x] = True
        tmp_gt[y][x] = 2
        for move in moves:
            ny = y + moves[move][0]
            nx = x + moves[move][1]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if tmp_gt[ny][nx] == 0:
                    dq.append([ny,nx])
    for r in range(N):
        for c in range(M):
            if tmp_gt[r][c] == 0:
                cnt += 1
    return cnt

# def make_walls(cnt):
#     global wall_idx
#     global answer
#     if cnt == 3:
#         print(wall_idx)
#         answer = max(answer, bfs(wall_idx,virus_idx))
#         wall_idx = []
#         return
    
#     for r in range(N):
#         for c in range(M):
#             if gt[r][c] == 0 and [r,c] not in wall_idx:
#                 wall_idx.append([r,c])
#                 make_walls(cnt+1)

N, M = map(int,input().split())
gt = []
for _ in range(N):
    gt.append(list(map(int,input().split())))
moves = {1:(0,1),2:(1,0),3:(0,-1),4:(-1,0)}
    
virus_idx = []
wall_cnt = 0
for r in range(N):
    for c in range(M):
        if gt[r][c] == 2:
            virus_idx.append([r,c])
        elif gt[r][c] == 1:
            wall_cnt += 1
answer = 0
# for a1 in range(N*M):
#     for a2 in range(N*M):
#         for a3 in range(N*M):
#             r1, c1 = divmod(a1,M)
#             r2, c2 = divmod(a2,M)
#             r3, c3 = divmod(a3,M)
#             wall_idx = [[r1,c1],[r2,c2],[r3,c3]]
#             if [r1,c1] != [r2,c2] and [r2,c2] != [r3,c3] and [r1,c1] != [r3,c3]:
#                 if gt[r1][c1] == 0 and gt[r2][c2] == 0 and gt[r3][c3] == 0:
#                     answer = max(answer, bfs(wall_idx,virus_idx))
for i in combinations(list(range(N*M)),3):
    r1, c1 = divmod(i[0],M)
    r2, c2 = divmod(i[1],M)
    r3, c3 = divmod(i[2],M)
    
    if gt[r1][c1] == 0 and gt[r2][c2] == 0 and gt[r3][c3] == 0:
        gt[r1][c1] = 1
        gt[r2][c2] = 1
        gt[r3][c3] = 1
        answer = max(answer, bfs(virus_idx))
        gt[r1][c1] = 0
        gt[r2][c2] = 0
        gt[r3][c3] = 0

print(answer)
            

        