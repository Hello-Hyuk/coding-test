import sys
from collections import deque
input = sys.stdin.readline

'''
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
'''
M, N, H = map(int, input().split())
t_boxes = []
init_idx = []
for _ in range(H):
    t_box = []
    for _ in range(N):
        t_box.append(list(map(int,input().split())))
    t_boxes.append(t_box)

# init idx of tomato
for h in range(H):
    for n in range(N):
        for m in range(M):
            if t_boxes[h][n][m] == 1:
                init_idx.append([h,n,m])
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
                
def bfs(idx,flag,day):
    dq = deque(idx)
    move = {'up':(1,0,0),'down':(-1,0,0),'front':(0,-1,0),'back':(0,1,0),'right':(0,0,1),'left':(0,0,-1)}
    next_idx = [] 
    
    while dq:
        h,n,m = dq.popleft()
        visited[h][n][m] = True
        for i in move:
            nh = h + move[i][0]
            nn = n + move[i][1]
            nm = m + move[i][2]
            
            if 0<= nh < H and 0<= nn < N and 0<= nm < M:
                if not visited[nh][nn][nm] and t_boxes[nh][nn][nm] == 0:
                    visited[nh][nn][nm] = True
                    t_boxes[nh][nn][nm] = 1
                    next_idx.append([nh,nn,nm])
    if not next_idx:
        flag = True
    return next_idx, flag, day+1

flag = False
days = -1

while not flag:
    init_idx, flag, days = bfs(init_idx,flag,days)
    
# check left tomatoes
for h in range(H):
    for n in range(N):
        for m in range(M):
            if t_boxes[h][n][m] == 0:
                days = -1
                break
if days == 0 and t_boxes[0][0][0] == -1: 
    days = -1
print(days)