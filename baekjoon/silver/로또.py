# 로또
# https://www.acmicpc.net/problem/6603

def dfs(n, start, arr):
    if n == 6:
        print(*arr)
        return
    for i in range(start, K):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, i+1, arr+[S[i]])
            visited[i] = 0
    
n = 0
while True:
    if n != 0:
        print()
    S = list(map(int, input().split()))
    K = S.pop(0)
    if K == 0:
        break
    visited = [0] * K
    dfs(0, 0, [])
    n += 1

