import sys
from collections import deque

def bfs():
    visited = [False] * 10000
    dq = deque([(A, '')])
    visited[A] = True

    while dq:
        num, operator = dq.popleft()
        if num == B:
            print(operator)
            break
        # D
        if not visited[num*2 % 10000]:
            visited[num*2 % 10000] = True
            dq.append((num*2 % 10000, operator+"D"))
        # S
        if not visited[(num-1) % 10000]:
            visited[(num-1) % 10000] = True
            dq.append(((num-1) % 10000, operator+"S"))
        # L  
        if not visited[num % 1000 * 10 + num//1000]:
            visited[num % 1000*10 + num//1000] = True
            dq.append((num % 1000*10 + num//1000, operator+"L"))
        # R
        if not visited[num % 10*1000 + num//10]:
            visited[num % 10*1000 + num//10] = True
            dq.append((num % 10*1000 + num//10, operator+"R"))
        
n = int(sys.stdin.readline())

for _ in range(n):
    A, B = map(int, sys.stdin.readline().split())
    bfs()
