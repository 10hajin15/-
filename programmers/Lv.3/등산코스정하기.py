# 등산코스 정하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118669
import heapq
from math import inf

def solution(n, paths, gates, summits):

    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    
    is_summit = [False] * (n+1)
    for summit in summits:
        is_summit[summit] = True
        
    distance = [inf] * (n+1)
    queue = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(queue, [0, gate])
    
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist or is_summit[now]:
            continue
        for i, cost in graph[now]:
            cost = max(distance[now], cost)
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(queue, [cost, i])
    
    result = [-1, inf]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]
    
    return result