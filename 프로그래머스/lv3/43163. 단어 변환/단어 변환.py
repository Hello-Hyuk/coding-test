from collections import deque

def solution(begin, target, words):
    dq = deque([(begin, 0)])
    visited = [False] * len(words)
    while dq:
        word, cnt = dq.popleft()
        if word == target:
            return cnt        
        for i in range(len(words)):
            if not visited[i]:
                tmp = 0
                for j in range(len(word)):
                    if words[i][j] != word[j]:
                        tmp += 1
                if tmp == 1:
                    dq.append([words[i], cnt+1])
                    visited[i] = True
    
    return 0

