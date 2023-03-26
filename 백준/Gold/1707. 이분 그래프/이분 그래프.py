import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
K = int(input())

def dfs(start, group):
    global answer
    # 만약 사이클이 true라면 재귀탈출
    if answer:
        return
    visited[start] = group  # 해당 그룹으로 등록
    for i in nodes[start]:
        if not visited[i]:
            dfs(i, -group)  # 다른 그룹으로 설정
        elif visited[start] == visited[i]:  # 인접한데 같은 그룹이라면
            answer = True  # 에러값 True
            return  # 그후 재귀 리턴
         
for _ in range(K):
    V, E = map(int, input().split())
    visited = [False] * (V+1)
    nodes = [[] for _ in range(V+1)]
    answer = False
    for _ in range(E):
        i, j = map(int,input().split())
        nodes[i].append(j)
        nodes[j].append(i)
        
    for i in range(1,V+1):
        if not visited[i]:
            dfs(i,1)
            if answer:
                break
    if answer: print("NO")
    else : print("YES")
    
    
# 5
# |
# 1 - 2 - 5
#     |  \
#     3 - 4

# 1 -3
#    |
#    2