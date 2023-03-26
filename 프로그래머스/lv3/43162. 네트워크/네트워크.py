def solution(n, computers):
    visited = [False] * n
    answer = 0
    def dfs(i):
        visited[i] = True
        for r in range(n):
            if computers[i][r] == 1 and i != r and visited[r] == False:
                dfs(r)

    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer += 1

    return answer