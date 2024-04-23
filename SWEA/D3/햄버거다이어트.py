import sys
sys.stdin = open("input.txt", "r")

def dfs(n, taste, kcal):
    global ans
    if kcal > L:
        return
    if n == N:
        ans = max(ans, taste)
        return  
    dfs(n+1, taste+info[n][0], kcal+info[n][1])
    dfs(n+1, taste, kcal)

T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    info = []
    for _ in range(N):
        a, b = map(int, input().split())
        info.append([a, b])
    ans = 0
    dfs(0, 0, 0)
    print(f"#{test_case} {ans}")