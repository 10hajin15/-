# 전기버스
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

############# 첫번째 풀이 #############
# for test_case in range(1, int(input())+1):
#     K, N, M = map(int, input().split())
#     c = list(map(int, input().split()))
#     idx = ans = 0
#     oil = K
#     for i in range(1, N+1):
#         oil -= 1
#         if oil < 0:
#             ans = 0
#             break
#         if i == N:
#             break
#         if i in c:
#             if idx < len(c):
#                 if idx == len(c)-1:
#                     if i+oil < N:
#                         oil = K
#                         ans += 1
#                 elif i+oil < c[idx+1]:
#                     ans += 1
#                     oil = K
#                 idx += 1

#     print(f"#{test_case} {ans}")

T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    lst = [0] + list(map(int, input().split())) + [N]

    ans = start = 0
    for i in range(1, M+2):
        if lst[i] - lst[i-1] > K:
            ans = 0
            break
        if lst[i] - start > K:
            start = lst[i-1]
            ans += 1

    print(f"#{test_case} {ans}")