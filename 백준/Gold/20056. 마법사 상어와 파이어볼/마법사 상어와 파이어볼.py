import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
gt = [[[] for _ in range(N)] for _ in range(N)]
moves = {0:(-1,0),1:(-1,1),2:(0,1),3:(1,1),4:(1,0),5:(1,-1),6:(0,-1),7:(-1,-1)}
fire_balls = []
# ri, ci, mi, si, di
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    fire_balls.append([r-1,c-1,m,s,d])

for _ in range(K):
    while fire_balls:
        r,c,m,s,d = fire_balls.pop(0)
        nr = (r + moves[d][0] *s) % N
        nc = (c + moves[d][1] *s) % N
        gt[nr][nc].append([m,s,d])
    for r in range(N):
        for c in range(N):
            if len(gt[r][c]) > 1:
                flag = False
                cmp = gt[r][c][0][2] % 2
                sum_m, sum_s, len_gt = 0, 0, len(gt[r][c])
                while gt[r][c]:
                    m,s,d = gt[r][c].pop(0)
                    sum_m += m
                    sum_s += s
                    if cmp != d % 2:
                        flag = True
                if sum_m//5:
                    for move in range(0+flag,8,2):
                        fire_balls.append([r,c,sum_m//5,sum_s//len_gt,move])        
            elif len(gt[r][c]) == 1:
                fire_balls.append([r,c]+gt[r][c].pop(0))
                
print(sum([f[2] for f in fire_balls]))                    