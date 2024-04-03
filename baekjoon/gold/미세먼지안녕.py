# 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

air = []
for i in range(R):
    for j in range(1):
        if arr[i][j] == -1:
            air.append(i)

for _ in range(T):
    temp = [[0] * C for _ in range(R)]
    temp[air[0]][0] = temp[air[1]][0] = -1

    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                dust = arr[i][j] // 5
                cnt = 0
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        temp[ni][nj] += dust
                        cnt += 1
                temp[i][j] += (arr[i][j] - (dust*cnt))
    arr = temp

    temp = [[0] * C for _ in range(R)]
    temp[air[0]][0] = temp[air[1]][0] = -1
    # 공기청정기 가동
    for i in range(R):
        for j in range(C):
            if i == 0:
                if j == C-1:
                    temp[i][j] = arr[i+1][j]
                else:
                    temp[i][j] = arr[i][j+1]
            elif i == air[0] or i == air[1]:
                if j < 2:
                    continue
                else:
                    temp[i][j] = arr[i][j-1]
            elif i == R-1:
                if j == C-1:
                    temp[i][j] = arr[i-1][j]
                else:
                    temp[i][j] = arr[i][j+1]
            elif j == 0:
                if i < air[0]:
                    temp[i][j] = arr[i-1][j]
                elif i > air[1]:
                    temp[i][j] = arr[i+1][j]
            elif j == C-1:
                if i < air[0]:
                    temp[i][j] = arr[i+1][j]
                elif i > air[1]:
                    temp[i][j] = arr[i-1][j]
            else:
                temp[i][j] = arr[i][j]
    arr = temp

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)