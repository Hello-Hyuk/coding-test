import sys
import copy
input = sys.stdin.readline


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if (0 <= nx < 4 and 0 <= ny < 4) and [nx,ny] != [sx,sy]:
                board[f_x][f_y][1] = nd
                board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
                break
    # 상어 먹음
    s_d = board[sx][sy][1]
    for i in range(1, 5):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))
            
board = [[] for _ in range(4)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish
max_score = 0
dfs(0, 0, 0, board)
print(max_score)

##### 내코드

# (x,y)
# 각 물고기 (번호 (1<=<=16) 독립, 8 방향)
# 청소년 상어 (0,0) 물고기 먹고 시작 , 방향 (0,0) 물고기 방향
# 물고기 이동
# 1. 번호가 작은 물고기 순 1칸 이동
#     a. 이동가능 : 빈칸, 다른물고기 있는칸
#     b. 이동 불가능 : 상어, 경계 넘어가는경우 
'''
각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 
만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 
그 외의 경우에는 그 칸으로 이동을 한다. 
물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.
'''
# 2. 상어 이동
'''
방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다
if 칸에 물고기 존재 -> 물고기 먹고, 물고기 방향 얻기 (단, 이동중 물고기는 먹지 않음)
물고기가 없는 칸 이동 불가
if 이동 할 수 있는 칸 없음 -> 종료
'''
# def dfs(shark_dir,shark_idx,fish_list,gt):
#     global max_score
#     print("-----------------------------")
#     max_score = max(max_score,gt[shark_idx[0]][shark_idx[1]][1])
#     for fish in fish_list:
#         fish_idx = fish_list[fish]
#         #print("fishidx",fish,fish_idx)
#         dir = gt[fish_idx[0]][fish_idx[1]][1]
#         #print("afaf",fish_idx,dir)
#         cnt = 0
#         while cnt < 8:
#             nr = fish_idx[0] + moves[dir][0]
#             nc = fish_idx[1] + moves[dir][1]
            
#             if 0 <= nr < 4 and 0 <= nc < 4 :
#                 if not gt[nr][nc]:
#                     fish_list[fish] = [nr,nc]
#                     gt[nr][nc] = gt[fish_idx[0]][fish_idx[1]]
#                     gt[fish_idx[0]][fish_idx[1]] = []
#                     break
#                 elif gt[nr][nc][0] != 100:
#                     gt_tmp = gt[nr][nc]
#                     change_fish_num = gt[nr][nc][0]
#                     change_fish_idx = [nr,nc]
#                     # swap
#                     gt[nr][nc] = [fish,dir]
#                     gt[fish_idx[0]][fish_idx[1]] = gt_tmp
#                     fish_list[change_fish_num] = fish_idx
#                     fish_list[fish] = change_fish_idx
#                     break
#             dir = (dir+1)%9
#             if dir == 0:
#                 dir += 1
#             cnt += 1
#         #for i in gt:
#             #print(*i)
#     # shark moves
#     # 2. 상어 이동
#     #print("---------shark move -----------")
#     #print(shark_dir,shark_idx)
#     for i in gt:
#         print(*i)
#     shark_move_idx = []
#     cnt = 0
#     while 1:
#         cnt += 1
#         sr = shark_idx[0] + moves[shark_dir][0] * cnt
#         sc = shark_idx[1] + moves[shark_dir][1] * cnt
#         if 0 <= sr < 4 and 0 <= sc < 4 and gt[sr][sc]:
#             shark_move_idx.append([sr,sc])
#         else :
#             break
    
#     print("afdsasdafds",shark_move_idx)
#     if shark_move_idx:
#         for smi in shark_move_idx:
#             snr = smi[0]
#             snc = smi[1]
#             #print("get",gt[snr][snc][1])
#             shark_dir = gt[snr][snc][1]
#             fish_num = gt[snr][snc][0]
#             ans = fish_num + gt[shark_idx[0]][shark_idx[1]][1]
#             gt[shark_idx[0]][shark_idx[1]] = []
#             shark_idx = fish_list.pop(fish_num)
#             gt[shark_idx[0]][shark_idx[1]] = [100, ans]
#             print("move",smi)
#             for i in gt:
#                 print(*i)
#             dfs(shark_dir,shark_idx,copy.deepcopy(fish_list),copy.deepcopy(gt))

# max_score = 0
# gt = []
# moves = {1:(-1,0),2:(-1,-1),3:(0,-1),4:(1,-1),5:(1,0),6:(1,1),7:(0,1),8:(-1,1)}
# for _ in range(4):
#     a, da, b, db, c, dc, d, dd = map(int,input().split())
#     gt.append([[a,da],[b,db],[c,dc],[d,dd]])
# # init process
# shark_dir = gt[0][0][1]
# shark_idx = [0,0]
# gt[0][0] = [100,gt[0][0][0]]

# fish_list = {}
# for r in range(4):
#     for c in range(4):
#         if gt[r][c][0] != 100:
#              fish_list[gt[r][c][0]] = [r,c]
             
# fish_list = dict(sorted(fish_list.items()))

# dfs(shark_dir,shark_idx,fish_list,gt)
# print(max_score)    