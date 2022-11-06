##  my
from heapq import heappop, heappush
from collections import defaultdict
def solution(n, paths, gates, summits):
    summits.sort()
    summits_set = set(summits)
    pq = []
    visited=[float('inf')] * (n+1) ## diff
    # graph 세팅
    graph = defaultdict(list)
    for a,b,dist in paths:
        graph[a].append((dist,b))
        graph[b].append((dist,a))

    for gate in gates:
        visited[gate]=0
        heappush(pq,(0,gate))
    
    while pq:
        intensity, now = heappop(pq)
        if now in summits_set or intensity > visited[now]:
            continue

        # 이번 위치에서 이동할 수 있는 곳으로 이동
        for weight, to in graph[now]:
            # to 위치에 더 작은 intensity로 도착할 수 있다면 큐에 넣지 않음
            # (출입구는 이미 0으로 세팅되어있기 때문에 방문하지 않음)
            new_intensity = max(intensity, weight)
            if new_intensity < visited[to]:
                visited[to] = new_intensity
                heappush(pq, (new_intensity, to))
                
    # 구한 intensity 중 가장 작은 값 반환
    min_intensity = [0, float('inf')]
    for summit in summits:
        if visited[summit] < min_intensity[1]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]

    return min_intensity