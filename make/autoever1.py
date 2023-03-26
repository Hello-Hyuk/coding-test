import sys
from math import inf
# max_weight : M
# 1 <= r, c, h <= 50 
# 2*(rc+rh+ch) 가 최소
# sorted(list, key=lambda x : (x[0],x[1],x[2]))
# sorted(list)
# 100 -> 4, 5, 5
# 12345 -> 21, 21, 28

M = int(sys.stdin.readline())

# 1, 1, 100  201
# 2, 2, 25   104 
# 3, 3, 12   81
# 4, 4, 7    72
# 5, 5, 4    65
# 6, 6, 3    72
# 7, 7, 3    91
# 8, 8, 2    96
# 9, 9, 2    117
# 10 10 1    120 

# 12345
# print(21*21)
# print(12348//441)
# print(12349%441)

r,c,h = 0,0,0
min_size = inf
ans = []

while r*c <= M:
    r += 1
    c += 1
    
    if M%(r*c)>0:
        h = (M//(r*c))+1
    elif M%(r*c) == 0:
        h = M//(r*c)
    cur_size = r*c+r*h+c*h
    
    if cur_size == min(min_size,cur_size):
        min_size = cur_size
        ans = [r,c,h]
    else :
        break

ans = sorted(ans)
print(*ans)