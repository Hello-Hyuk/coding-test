import sys
input = sys.stdin.readline

N = int(input())    

num = N

answer = 0
if num//5 > 0:
    time = num//5
else :
    time = 0
    
min_time = 1000**6
for i in range(time+1):
    num_left = N - (i*5)
    if num_left%3 == 0:
        min_time = min(min_time, i+num_left//3)
        
if min_time == 1000**6:
    print(-1)
else :
    print(min_time)