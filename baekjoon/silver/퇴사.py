# 퇴사
# https://www.acmicpc.net/problem/14501
import sys
input = sys.stdin.readline
n = int(input())
schedule = []
dp = [0] * n

for _ in range(n):
    t, p = map(int, input().split())
    schedule.append((t, p))

for i in range(n):
    t, p = schedule[i]
    if t+i > n:
        continue

    dp[i] = max(dp[i], p)
    t += i
    while t < n:
        if schedule[t][0] + t > n:
            t += 1
            continue
        dp[t] = max(dp[i] + schedule[t][1], dp[t]) 
        t += 1

print(max(dp))

# import sys
# input = sys.stdin.readline

# n = int(input())
# schedule = []

# for _ in range(n):
#     t, p = map(int, input().split())
#     schedule.append((t, p))

# # 각 날짜별 최대 이익을 저장할 리스트 초기화
# dp = [0] * (n + 1)

# for i in range(n - 1, -1, -1):  # 거꾸로 탐색
#     t, p = schedule[i]

#     # 현재 날짜에 상담을 할 수 있는 경우
#     if i + t <= n:
#         # 상담을 했을 때의 이익과 상담을 하지 않았을 때의 이익 중 큰 값을 선택
#         dp[i] = max(p + dp[i + t], dp[i + 1])
#     else:
#         # 현재 날짜에 상담을 할 수 없는 경우
#         dp[i] = dp[i + 1]

# print(dp[0])

# import sys
# input = sys.stdin.readline
# n = int(input())

# schedule = [list(map(int, input().split())) for i in range(n)]

# dp = [0 for i in range(n+1)]

# for i in range(n):
#     for j in range(i + schedule[i][0], n+1):
#         if dp[j] < dp[i] + schedule[i][1]:
#             dp[j] = dp[i] + schedule[i][1]

# print(dp[-1])