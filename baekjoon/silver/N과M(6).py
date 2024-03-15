# N과 M ()
# https://www.acmicpc.net/problem/15655

def dfs(n, start, lst):
    if n == M:
        print(*lst)
        return
    for i in range(start, N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, i+1, lst+[arr[i]])
            visited[i] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * N
dfs(0, 0, [])