import sys
input = sys.stdin.readline
'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''
N= int(input()) 
infos = []
for _ in range(N):
    infos.append(list(map(int,input().split())))

infos = sorted(infos, key=lambda x : (x[0]))
infos = sorted(infos, key=lambda x : (x[1]))

answer = 0
tmp_num = 0
for i in range(N):
    if tmp_num <= infos[i][0]:
        answer += 1
        tmp_num = infos[i][1]
print(answer)