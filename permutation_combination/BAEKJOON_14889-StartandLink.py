import sys
from itertools import permutations, combinations

gt = []
n = int(sys.stdin.readline())
for _ in range(n):
    gt.append(list(map(int, sys.stdin.readline().split())))

team_list = []
for i in combinations(list(range(n)),n//2):
    team_list.append(i)
team_start = team_list[:len(team_list)//2]
team_link = team_list[:len(team_list)//2-1:-1]

stat = []
for i in range(len(team_start)):
    start_stat = 0
    link_stat = 0  
    for j, k in zip(permutations(team_start[i],2),permutations(team_link[i],2)):
        start_stat += gt[j[0]][j[1]]
        link_stat += gt[k[0]][k[1]]
    stat.append(abs(start_stat-link_stat))

print(min(stat))