import sys
input = sys.stdin.readline
from collections import deque
    
S = deque(input().rstrip())
T = deque(input().rstrip())

while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S == T:
        print(1)
        exit()
print(0)