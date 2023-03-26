import sys
from collections import deque
input = sys.stdin.readline
'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

def bfs():
    dq = deque([(N,0)])
    while dq:
        idx, step = dq.popleft()
        if idx == K:
            print(step)
            break
        for move in (idx-1,idx+1,idx*2):
            if 0 <= move < 100001 and not place[move]:
                place[move] = step+1
                dq.append([move, step+1])
        
N, K = map(int, input().split())
place = [0] * 100001     
bfs()