import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int, input().split())
stones, bags = [], []
for _ in range(N):
    heappush(stones, list(map(int,input().split())))
    #stones.append(list(map(int,input().split())))

for _ in range(K):
    bags.append(int(input()))
#stones.sort()
bags.sort()

# stone : Mass Value
# bag : C (Max weight)
answer, tmp = 0, []
for bag in bags:
    while stones and stones[0][0] <= bag:
        heappush(tmp, -stones[0][1])
        heappop(stones)
    if tmp:
        answer -= heappop(tmp)
print(answer) 