# 달팽이 숫자
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
for test_case in range(1, int(input())+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    dir = 0
    i = j = 0
    for num in range(1, n*n+1):
        arr[i][j] = num
        ni, nj = i+d[dir][0], j+d[dir][1]
        if 0<=ni<n and 0<=nj<n and not arr[ni][nj]:
            i, j = ni, nj
        else:
            dir = (dir+1)%4
            ni, nj = i+d[dir][0], j+d[dir][1]
            if 0<=ni<n and 0<=nj<n and not arr[ni][nj]:
                i, j = ni, nj

    print(f"#{test_case}")
    for i in range(n):
        print(*arr[i])