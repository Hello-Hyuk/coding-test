import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
# 서류 성적, 면접 성적
test_cases = []
for _ in range(T):
    N = int(input())
    test_case = []
    for _ in range(N):
        test_case.append(list(map(int,input().split())))
    test_case.sort(key = lambda x : x[0])
    ans = 1
    tmp = test_case[0][1]
    for i in test_case[1:]:
        if i[1] < tmp:
            ans += 1
            tmp = i[1]
    print(ans)