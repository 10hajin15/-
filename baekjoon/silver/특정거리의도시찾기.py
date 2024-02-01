# 특정 거리의 도시찾기
# https://www.acmicpc.net/problem/18352
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, k, x = map(int, input().split())
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

dijkstra(x)

count = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        count += 1
if count == 0:
    print(-1)