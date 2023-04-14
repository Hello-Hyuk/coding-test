import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    wood = list(map(int,input().split()))
    wood.sort()
    new_wood = []
    new_wood.extend(wood[0::2])
    tmp = wood[1::2]
    new_wood.extend(tmp[::-1])
    
    idx = 0
    answer = 0
    while 1:
        idx = (idx+1)%len(new_wood)
        answer = max(answer,abs(new_wood[idx]-new_wood[idx-1]))
        if idx == 0:
            break
    print(answer)
        