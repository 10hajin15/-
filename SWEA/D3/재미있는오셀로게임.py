# 재미있는 오셀로 게임
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2-1][N//2-1] = arr[N//2][N//2] = 2
    arr[N//2-1][N//2] = arr[N//2][N//2-1] = 1
    
    for i in range(M):
        x, y, stone = map(int, input().split())
        arr[y-1][x-1] = stone
        for di, dj in ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)):
            ni, nj = y-1+di, x-1+dj
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj] > 0 and arr[ni][nj] != stone:
                    tmp = [(ni, nj)]
                    while True:
                        ni, nj = ni+di, nj+dj
                        if ni<0 or ni>=N or nj<0 or nj>=N:
                            break
                        if arr[ni][nj] == 0:
                            break
                        if arr[ni][nj] == stone:
                            if tmp:
                                for i, j in tmp:
                                    arr[i][j] = stone
                            break
                        tmp.append((ni, nj))
                    

    B = W = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                B += 1
            elif arr[i][j] == 2:
                W += 1

    print(f'#{test_case} {B} {W}')