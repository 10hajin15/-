# N과 M (2)
# https://www.acmicpc.net/problem/15650
def dfs(depth, start, lst):
    if depth == m:
        ans.append(lst)
        return
    for i in range(start, n+1):
        dfs(depth+1, i+1, lst+[i])

n, m = map(int, input().split())
ans = []
dfs(0, 1, [])   # 멀티트리

for a in ans:
    print(*a)

# def dfs(n, lst):
#     if n > N:
#         if len(lst) == M:
#             ans.append(lst)
#         return
#     dfs(n+1, lst+[n])       # 선택하는 경우
#     dfs(n+1, lst)           # 선택하지 않는 경우

# N, M = map(int, input().split())
# ans = []
# dfs(1, [])    # 이진트리
# for lst in ans:
#     print(*lst)