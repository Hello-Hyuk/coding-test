from collections import deque

def solution(cap, n, deliveries, pickups):
    print(cap, n, deliveries, pickups)
    de = deque(deliveries)
    pi = deque(pickups)
    
    de_idx = cap
    pi_idx = cap
    
    answer = []
    print("init de and pi",de,pi)
    while de or pi :
        l_d = len(de)
        l_p = len(pi)
        for i in range(l_d):
            if de[l_d-i-1] == 0:
                de.pop()
            else : break
        for i in range(l_p):
            if pi[l_p-i-1] == 0:
                pi.pop()
            else : break
            
        print(f"recursive pop\nde : {de}\npi : {pi}")
        
        dist = max(len(de), len(pi))
        # delivery
        for i in range(len(de)):
            idx = len(de)-i-1
            de_idx -= de[idx]
            if de_idx > 0 :
                de[idx] = 0
                continue
            if de_idx <= 0 :
                de[idx] = abs(de_idx)
                de_idx = cap 
                break
        # pickup
        for i in range(len(pi)):
            idx = len(pi)-i-1
            pi_idx -= pi[idx]
            if pi_idx > 0 :
                pi[idx] = 0
                continue
            if pi_idx <= 0 :
                pi[idx] = abs(pi_idx)
                pi_idx = cap 
                break
        answer.append(dist)
    print("answer",answer)
    return sum(answer) *2

#solution(4,5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0])
#solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0])
solution(2, 2, [0,0], [0,4])