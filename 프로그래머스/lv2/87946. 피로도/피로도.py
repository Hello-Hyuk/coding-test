answer = 0
def dfs(k, rst, dungeons, visited):
    global answer
    answer = max(answer, rst)
    for i in range(len(dungeons)):
        if visited[i] == 0 and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], rst+1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    visited = [False]*len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer