# 목장 건설하기
# https://www.acmicpc.net/problem/14925

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans = max(ans, dp[i][j])

print(ans)