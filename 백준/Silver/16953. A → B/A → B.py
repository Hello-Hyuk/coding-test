import sys
input = sys.stdin.readline
from collections import deque

A, B = map(str,input().split())
A = deque(A)
B = deque(B)

answer = 1
while B:
    if B[-1] == '1':
        B.pop()
    else :
        tmp = int("".join(B))%2
        if tmp == 1:
            if A != B:
                break
        elif tmp == 0:
            B = deque(str(int("".join(B))//2))
    answer += 1
    if A == B:
        print(answer)
        exit()
print(-1)

