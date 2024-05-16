# 현주의 상자 바꾸기
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

for test_case in range(1, int(input())+1):
    N, Q = map(int, input().split())
    arr = [0]*N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        arr[L-1:R] = [i]*(R-L+1)
    print(f"#{test_case}", end=" ")
    print(*arr)