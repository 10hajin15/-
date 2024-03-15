# N과 M (4)
# https://www.acmicpc.net/problem/15652

def dfs(n, start, lst):
    if n == M:
        ans.append(lst)
        return
    for i in range(start, N+1):
        dfs(n+1, i, lst+[i])

N, M = map(int, input().split())
ans = []
dfs(0, 1, [])
for a in ans:
    print(*a)