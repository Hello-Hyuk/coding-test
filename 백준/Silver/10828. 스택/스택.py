import sys
input = sys.stdin.readline
from collections import deque
'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
N = int(input())
stack = deque([])
for _ in range(N):
    a = list(map(str,input().split()))
    if len(a) == 2:
        cmd, num = a[0], int(a[1])
    else : 
        cmd = a[0]
    if cmd == "push":
        stack.append(num)
    elif cmd == "pop":
        if not stack:
            print(-1)
        else : print(stack.pop())
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if stack:
            print(0)
        else :
            print(1)
    elif cmd == "top":
        if not stack:
            print(-1)
        else : print(stack[-1])