'''
R(뒤집기): 배열에 있는 수의 순서를 뒤집는 함수
D(버리기): 첫 번째 수를 버리는 함수 단, 빈배열때 실행 시 ERROR
'''
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    p = str(input().strip())
    n = int(input())
    _list = deque(input().rstrip()[1:-1].split(","))
    if n == 0:
        _list = deque()
    flag = 1
    for i in p:
        if i == 'R':
            flag *= -1
        elif i == 'D':
            if len(_list) != 0:
                if flag == 1:
                    _list.popleft()
                elif flag == -1:
                    _list.pop()
            else:
                print("error")
                flag = 0
                break
    if flag == 0:
        continue
    else :
        if flag == 1:
            print("["+",".join(_list)+"]")
        elif flag == -1:
            _list.reverse()
            print("["+",".join(_list)+"]")