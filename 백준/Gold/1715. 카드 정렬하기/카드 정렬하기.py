import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())
cards = []
ans = 0
for _ in range(T):
    heappush(cards,int(input()))   
    
if len(cards) == 1:
    print(0)
else :
    while len(cards) != 1:
        
        tmp = heappop(cards) + heappop(cards)
        ans += tmp
        heappush(cards,tmp)
        
    print(ans)