# 퇴사2
# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline

n = int(input())
schedule = []

for _ in range(n):
    t, p = map(int, input().split())
    schedule.append((t, p))

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    t, p = schedule[i]

    if i + t <= n:
        dp[i] = max(p + dp[i + t], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[0])