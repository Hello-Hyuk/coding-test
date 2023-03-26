from collections import deque

def solution(n, wires):
    res = 100
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    def bfs(node, node2):
        visited = [False] * (n+1) 
        dq = deque([node])
        visited[node] = True
        visited[node2] = True
        cnt = 1
        while dq :
            idx = dq.popleft()
            for _n in graph[idx]:
                if not visited[_n]:
                    dq.append(_n)
                    visited[_n] = True
                    cnt += 1
        return cnt
                
    for i in range(len(wires)):
        res = min(abs(bfs(wires[i][0],wires[i][1])-bfs(wires[i][1],wires[i][0])), res)

    return res