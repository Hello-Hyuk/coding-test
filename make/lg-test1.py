import numpy as np

def solution(g,t):
    tmp = g 
    for i in range(t):
        ans = []
        for row in tmp:
            r_list = list(reversed(row))
            ans.append(row + r_list)
        tmp = ans 
        for col in tmp[::-1]:
            ans.append(col)
    return ans
    
def solution_np(g,t):
    g_np = np.array(g)
    for _ in range(t):
        g_col_fliped = np.flip(g_np, axis=1)
        g_np = np.concatenate((g_np,g_col_fliped),axis=1)
        g_row_fliped = np.flip(g_np, axis=0)
        g_np = np.concatenate((g_np,g_row_fliped),axis=0)
    return g_np.tolist()

given = [[0,1,2],[4,0,4],[0,1,2]]
ti = 2
     
# 한번 결과 수행 시 
# given [[0,1,2],[4,0,4],[0,1,2]]
# step 1 : [[0,1,2,2,1,0],[4,0,4,4,0,4],[0,1,2,2,1,0]] (col 축 뒤집어서 붙이기)
# step 2 : [[0,1,2,2,1,0],  (row 축 뒤집어서 붙이기)
#           [4,0,4,4,0,4],
#           [0,1,2,2,1,0],
#           [0,1,2,2,1,0],
#           [4,0,4,4,0,4],
#           [0,1,2,2,1,0]]

print(solution(given,ti) == solution_np(given,ti))

