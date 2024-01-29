# 조립라인
# https://softeer.ai/practice/6287
import sys
input = sys.stdin.readline
n = int(input())

dp = [[0] * n for _ in range(2)]
work = [[], []]
switch = [[], []]
for i in range(n-1):
    a, b, atob, btoa = map(int, input().split())
    work[0].append(a)
    work[1].append(b)
    switch[0].append(atob)
    switch[1].append(btoa)

an, bn = map(int, input().split())

for i in range(n):
    if n == 1:
        dp[0][0] = an
        dp[1][0] = bn
        break
    if i == 0:
        dp[0][i] = work[0][i]
        dp[1][i] = work[1][i]
        continue
    if i == n-1:
        dp[0][i] = min(dp[0][i-1], dp[1][i-1] + switch[1][i-1]) + an
        dp[1][i] = min(dp[1][i-1], dp[0][i-1] + switch[0][i-1]) + bn
    else:
        dp[0][i] = min(dp[0][i-1], dp[1][i-1] + switch[1][i-1]) + work[0][i]
        dp[1][i] = min(dp[1][i-1], dp[0][i-1] + switch[0][i-1]) + work[1][i]

print(min(dp[0][-1], dp[1][-1]))

########## 다른 사람 풀이 ###########
# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = [[0,0] for _ in range(n)]

# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))
# dp[0] = [arr[0][0], arr[0][1]]

# for i in range(1, n):
#     dp[i][0] = min(dp[i-1][0], dp[i-1][1] + arr[i-1][3]) + arr[i][0]
#     dp[i][1] = min(dp[i-1][1], dp[i-1][0] + arr[i-1][2]) + arr[i][1]

# print(min(dp[-1]))