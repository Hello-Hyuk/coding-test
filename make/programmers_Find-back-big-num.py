from collections import deque

def solution(numbers):
    dq = deque()
    answer = [-1] * (len(numbers))
    cnt = 0
    for i in range(len(numbers)):
        cmp = numbers[i]
        while dq and dq[0][0] < cmp:
            idx = dq.popleft()
            answer[idx[1]] = cmp
             
        dq.appendleft([cmp,i])
    print(answer)
    return answer

#solution([2, 3, 3, 5])
solution([9, 1, 5, 3, 6, 2])