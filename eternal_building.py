import numpy as np

def solution(board, skill):
    board_np = np.array(board)
    result = np.zeros((board_np.shape[0]+1,board_np.shape[1]+1))
    
    for type, r1, c1, r2, c2, degree in skill:
        result[r1][c1] += degree if type == 2 else -degree
        result[r1][c2 + 1] += -degree if type == 2 else degree
        result[r2 + 1][c1] += -degree if type == 2 else degree
        result[r2 + 1][c2 + 1] += degree if type == 2 else -degree  
    
    for r in range(result.shape[0] - 1):
        for c in range(result.shape[1] - 1):
            result[r][c + 1] += result[r][c]
            
    for c in range(result.shape[1] - 1):
        for r in range(result.shape[0] - 1):
            result[r + 1][c] += result[r][c]
    
    rst = board_np + result[:result.shape[0]-1,:result.shape[1]-1]
    answer = len(list(np.where(rst>0))[0])
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
solution(board,skill)