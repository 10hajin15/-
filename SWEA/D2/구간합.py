# 구간 합
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    s_min = sum(arr)
    s_max = 0
    for i in range(N-M+1):
        s = sum(arr[i:i+M])
        s_min = min(s_min, s)
        s_max = max(s_max, s)

    print(f"#{test_case} {s_max-s_min}")