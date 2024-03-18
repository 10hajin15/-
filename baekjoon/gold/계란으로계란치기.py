# 계란으로 계란치기
# https://www.acmicpc.net/problem/16987
import sys
input = sys.stdin.readline

def dfs(n, cnt):
    global ans
    if n == N:
        ans = max(ans, cnt)
        return
    if egg[n][0] <= 0:
        dfs(n+1, cnt)
    else:
        flag = False
        for i in range(N):
            if i == n or egg[i][0] <= 0:
                continue
            flag = True
            egg[n][0] -= egg[i][1]
            egg[i][0] -= egg[n][1]
            dfs(n+1, cnt+int(egg[n][0] <= 0)+int(egg[i][0] <= 0))
            egg[n][0] += egg[i][1]
            egg[i][0] += egg[n][1]
        if flag == False:
            dfs(n+1, cnt)   

N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, 0)
print(ans)
