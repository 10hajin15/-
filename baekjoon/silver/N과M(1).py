# N과 M (1)
# https://www.acmicpc.net/problem/15649
def dfs(n, lst):
    if n == M:
        print(*lst)
        return
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, lst+[i])
            visited[i] = 0

N, M = map(int, input().split())
visited = [0] * (N+1)
dfs(0, [])