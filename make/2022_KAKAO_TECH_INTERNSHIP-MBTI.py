import numpy as np

def solution(survey, choices):
    score = [0]*8
    answer = ""
    chractor = np.array(["R","T","C","F","J","M","A","N"])
    
    for i in enumerate(survey):
        not_agree = i[1][0]
        agree = i[1][1]
        choice = choices[i[0]]
        
        not_agree_idx = (np.where(chractor == not_agree))[0][0]
        agree_idx = (np.where(chractor == agree))[0][0]
        
        if choice > 4 :
            score[agree_idx] += abs(choice-4)
        else :
            score[not_agree_idx] += abs(choice-4)
            
    for i in range(4):
        diff = score[2*i] - score[2*i+1]
        
        if diff >= 0 :
            answer += chractor[2*i]
        else :
            answer += chractor[2*i+1]

    return answer