# 부분수열의 합
# https://www.acmicpc.net/problem/1182

# n: 배열의 인덱스
def dfs(n, total, cnt):
    global ans
    if n == N:
        if cnt > 0 and total == S:
            ans += 1
        return
    dfs(n+1, total+arr[n], cnt+1)   # 포함하는 경우
    dfs(n+1, total, cnt)            # 포함하지 않는 경우
    

N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
ans = 0
dfs(0, 0, 0)
print(ans)