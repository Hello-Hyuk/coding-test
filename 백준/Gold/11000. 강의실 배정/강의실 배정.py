import sys
input = sys.stdin.readline
from heapq import heappop,heappush

N = int(input())
lect = []
for _ in range(N):
    lect.append(list(map(int,input().split())))
lect.sort()
lect_idx = []
heappush(lect_idx,lect[0][1])
for i in range(1,N):
    if lect_idx[0] > lect[i][0]:
        heappush(lect_idx,lect[i][1])
    else:
        heappop(lect_idx)
        heappush(lect_idx, lect[i][1])
print(len(lect_idx))