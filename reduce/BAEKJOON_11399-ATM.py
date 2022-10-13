import sys
from functools import reduce

n = int(sys.stdin.readline())
ans = 0 
stime = sorted(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    ans += reduce(lambda x, y : x + y,stime[:i+1],0)
    
print(ans)