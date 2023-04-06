import sys
from collections import deque
input = sys.stdin.readline
'''
'.'은 빈 칸을 의미하고, 
'#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 
'O'는 구멍의 위치를 의미한다. 
'R'은 빨간 구슬의 위치, 
'B'는 파란 구슬의 위치이다.
'''
def move_ball(move, y, x):
    cnt = 0
    while gt[y+moves[move][0]][x+moves[move][1]] != '#' and gt[y][x] != 'O':
        y += moves[move][0]
        x += moves[move][1]
        cnt += 1
    return cnt,y,x
            
def bfs(r_idx,b_idx):
    dq = deque([[r_idx[0],r_idx[1],b_idx[0],b_idx[1],0]])
    visited = set((r_idx[0],r_idx[1],b_idx[0],b_idx[1]))
    while dq:
        rr,rc,br,bc,cnt = dq.popleft()
        if [rr,rc] == h_idx:
            return cnt
        if cnt > 10:
            break
        for move in moves:
            red_cnt, nrr, nrc = move_ball(move, rr, rc)
            blue_cnt, nbr, nbc = move_ball(move, br, bc)
            if (nrr,nrc,nbr,nbc) not in visited:
                if gt[nbr][nbc] == 'O':
                    continue
                if [nrr,nrc] == [nbr,nbc]:
                    if red_cnt > blue_cnt:
                        nrr -= moves[move][0]
                        nrc -= moves[move][1]
                    else :
                        nbr -= moves[move][0]
                        nbc -= moves[move][1]
                dq.append([nrr,nrc,nbr,nbc,cnt+1])
                visited.add((nrr,nrc,nbr,nbc))
    return -1
    
moves = {1:(-1,0),2:(0,1),3:(1,0),4:(0,-1)}
N, M = map(int,input().split())
gt = []
for _ in range(N):
    gt.append(input().strip())
r_idx, b_idx, h_idx = 0,0,0
for r in range(N):
    for c in range(M):
        if gt[r][c] == 'R':
            r_idx = [r,c]
        elif gt[r][c] == 'B':
            b_idx = [r,c]
        elif gt[r][c] == 'O':
            h_idx = [r,c]
answer = 0
print(bfs(r_idx,b_idx))

'''
7 7
#######
#...RB#
#.#####
#.....#
#####.#
#O....#
#######
'''