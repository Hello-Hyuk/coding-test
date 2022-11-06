from itertools import combinations_with_replacement
import numpy as np

def solution(n, info):
    # 명중률 비교 -> 높은 점수에 많이 맞춘사람이 k점
    # 명중률 같을 시  -> 어피치 k점
    info_np = np.array(info)
    answer = [[]]
    max_diff = 0
    for combi in combinations_with_replacement(range(11), n): 
        info2 = [0] * 11
        for i in combi:
            info2[10-i] += 1
        print(info,info2)
        info2_np = np.array(info2)
        # # compare
        a_point = 0
        r_point = 0
        for i in range(11):
            if info2[i] > info[i]:
                r_point += 10-i
            elif info2[i] < info[i]:
                a_point += 10-i      
            else:
                if info[i] != 0:
                    a_point += 10-i
        diff = r_point - a_point
        if diff > 0 and max_diff >= diff:
            if answer:
                if answer[-1][0] == diff:
                    answer.append((diff,info2))
                else:
                    answer = [(diff,info2)]
                    max_diff = diff
            else :
                answer.append((diff,info2))
                max_diff = diff
        print("af",answer)
        # comp = info_np - info2_np
        # a_point_idx = np.array(np.where(comp>0))
        # r_point_idx = np.array(np.where(comp<0))
        
        # diff =  np.sum(abs(r_point_idx-10)) - np.sum(abs(a_point_idx-10))
        
        # if diff > 0 and diff >= max_diff:
        #     max_diff = diff
        #     answer.append(info2)
    # if max_diff == 0:
    #     answer.append(-1)
    # answer_np = np.array(answer)
    
    # for i in range(11):
    #     print("asfd",answer_np)
    #     idx = np.array(np.where(answer_np[:,10-i]>0))
    #     if len(idx[0]) == 1:
    #         answer = np.squeeze((answer_np[idx[0],:])).tolist()
    #         break
            
    return answer
        
    
print("answer",solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
