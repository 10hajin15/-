# 부분 수열의 합
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

def dfs(n,total,cnt):
    global ans
    if n == N:
        if cnt > 0 and total == K:
            ans += 1
        return
    dfs(n+1, total+arr[n],cnt+1)
    dfs(n+1, total, cnt)

for test_case in range(1, int(input())+1):
    ans = 0
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    dfs(0,0,0)
        
    print(f"#{test_case} {ans}")