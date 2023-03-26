from collections import deque
def solution(s):
    
    if s[0] == ")":
        return False
    dq = deque([[s[0]]])
    for i in range(1,len(s)):
        if s[i] == ")":
            if not dq:
                return False
            else : dq.popleft()
        elif s[i] == "(":
            dq.append("(")
    
    if dq :
        return False
    else : return True
