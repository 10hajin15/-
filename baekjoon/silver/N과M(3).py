# N과 M (3)
# https://www.acmicpc.net/problem/15651

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for i in range(1, N+1):
        dfs(n+1, lst+[i])

N, M = map(int, input().split())
ans = []
dfs(0, [])
for a in ans:
    print(*a)