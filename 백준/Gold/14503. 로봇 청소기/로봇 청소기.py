import sys
input = sys.stdin.readline

# 북 동 남 서
heading = {0:(0,-1),1:(1,0),2:(0,1),3:(-1,0)}
N,M = map(int,input().split())
r, c, d = map(int,input().split())

room = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    room.append(list(map(int,input().split())))

answer = 0

while 1:
    if not visited[r][c] and not room[r][c]:
        visited[r][c] = True
        answer += 1
    # 현재 칸의 주변칸 중 청소되지 않은 빈 칸이 있는 경우
    nr, nc = 0, 0
    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        if not visited[r+heading[d][1]][c+heading[d][0]] and not room[r+heading[d][1]][c+heading[d][0]]:
            nr = r+heading[d][1]
            nc = c+heading[d][0]
            break
    if nr and nc:
        r = nr
        c = nc
    else :
        if 0 <= r-heading[d][1] < N and 0 <= c-heading[d][0] < M:
            if not room[r-heading[d][1]][c-heading[d][0]]:
                r = r-heading[d][1]
                c = c-heading[d][0]
            else : break
        else : break
print(answer)