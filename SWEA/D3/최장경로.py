# 최장경로
def dfs(v, dist):
    global ans
    if dist > ans:
        ans = dist
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, dist+1) 
            visited[i] = 0   

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    ans = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print(f'#{test_case} {ans}')