import sys
import numpy as np

pic = int(sys.stdin.readline())
stu_num = int(sys.stdin.readline())
vote = list(map(int, sys.stdin.readline().split()))

answers = []

answer = np.array([[vote[0]],[1]])
print(answer.shape)
    
for i in vote[1:]:
    #print("check ans\n",answer)
    print("start\n",answer)
    print("new vote",i)
    print("list ",answer[0])
    
    if i in answer[0]:
        idx = np.where(answer[0]==i)[0][0]
        answer[0,idx] += 1
    # 신규등록
    if i not in answer[0] :
        if len(answer[0]) < 3 :
            print(len(answer[0]))
            answer = np.append(answer, [[i],[1]], axis=1)
        else : 
            print(len(answer[0]))
            delete_idx =  min(np.where(answer[1]==min(answer[1])))
            print("af",delete_idx)
            if len(delete_idx) > 1:
                print("delete_idx",delete_idx[0]) 
                answer = np.delete(answer,delete_idx[0],axis=1)
                answer = np.append(answer, [[i],[1]], axis=1)
            else :
                answer = np.delete(answer,0,axis=1)
                
    print("end\n",answer)

# print(answer[0])
print("hello",answer)
print(min(np.where(answer[1]==1)[0]))

#answers.sort()
print(' '.join(map(str,answers)))