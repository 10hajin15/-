# 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    dp = []
    for i in range(1, len(triangle)+1):
        dp.append([0] * i)
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[-1])