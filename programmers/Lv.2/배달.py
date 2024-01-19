# 배달
# https://school.programmers.co.kr/learn/courses/30/lessons/12978
import heapq
INF = int(1e9)

def dijkstra(graph, distance, start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    for i in range(len(road)):
        x, y, z = road[i]
        graph[x].append((y, z))
        graph[y].append((x, z))

    dijkstra(graph, distance, 1)

    count = 0
    for i in range(1, N+1):
        if distance[i] <= K:
            count += 1
    print('distance', distance)

    return count

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))