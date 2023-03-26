import sys
from collections import defaultdict
dx = [-1,0,1,0]
dy = [0,1,0,-1]  


def count_seat(idx):
    space_seat = [0] * n**2 
    space_near_seat = [0] * n**2 
      
    for a in idx:
        print("idx",a)
        # int to point
        j,i = get_idx(a)
        print("idx convert",j,i)
        for k in range(4):
            nx = i+dx[k] 
            ny = j+dy[k]
            if 0<=nx<n and 0<=ny<n and seat[ny][nx] == 0:
                space_seat[get_idx_rev(ny,nx)] += 1
    max_vote = max(space_seat)
    if space_seat.count(max_vote) > 1 and max_vote != 0:
        for q in enumerate(space_seat):
            if q[1] == max_vote:
                j,i = get_idx(q[0])
                for k in range(4):
                    nx = i+dx[k] 
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<n and seat[ny][nx] == 0:
                        space_near_seat[q[0]] += 1
        print("space_seat",space_seat)
        print("space_seat_near",space_near_seat)
        return space_near_seat
    return space_seat

def get_idx(i):
    global n
    j = i // n 
    k = i % n
    return j,k

def get_idx_rev(j,k):
    global n 
    return j * n + k

n = int(sys.stdin.readline())
invest = []
for _ in range(n**2):
    invest.append(list(map(int,sys.stdin.readline().split())))

seat = [[0]*n for _ in range(n)]

list_seat = [0] * n**2
#near_cnt = []

list_seat[get_idx_rev(1,1)] = invest[0][0]
seat[1][1] = invest[0][0]

for i in invest[1:]:
    tmp_seat = []
    print(f"{i[0]} voted {i[1:]}")
    for j in i[1:]:
        
        if j in list_seat:
            print("vote",j)
            tmp_seat.append(list_seat.index(j))
    _count_seat = count_seat(tmp_seat)
    
    ### 주변 자리갯수 세기
    
    print("주변 자리 개수",_count_seat)

    list_seat[_count_seat.index(max(_count_seat))] = i[0]
    r, c = get_idx(_count_seat.index(max(_count_seat)))
    seat[r][c] = i[0]

#invest.sort(key= lambda x : x[0])
print(seat)

invest_dic = defaultdict(list)

for i in invest:
    invest_dic[i[0]].append(i[1:])
#print(invest_dic)

preference_score = {1:1, 2:10, 3:100, 4:1000} 

ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            nx = i+dx[k] 
            ny = j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                #print(f"{seat[ny][nx]} in {(invest_dic[seat[j][i]])[0]}")
                if seat[ny][nx] in (invest_dic[seat[j][i]])[0]:
                    cnt += 1
        ans += preference_score[cnt]
print(ans)
