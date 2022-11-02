from collections import deque
def solution(queue1, queue2):
    answer = 0
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    sum1 = sum(deque1)
    sum2 = sum(deque2)
    goal = (sum1 + sum2)//2
    
    for _ in range(len(deque1)*3):
        diff = sum1 - sum2
        if goal*2 == abs(diff):
            return -1
        if diff == 0:
            return answer
        elif diff > 0:
            num = deque1.popleft() 
            deque2.append(num)
            sum1 -= num
            sum2 += num
            answer += 1
        elif diff < 0:
            num = deque2.popleft() 
            deque1.append(num)
            sum1 += num
            sum2 -= num
            answer += 1
    return -1