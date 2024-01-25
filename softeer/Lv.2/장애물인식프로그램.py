# 장애물 인식 프로그램
# https://softeer.ai/practice/6282
import sys
input = sys.stdin.readline

n = int(input())

maps = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global count
    maps[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if maps[nx][ny] == 1:
            count += 1
            dfs(nx, ny)
    return

count = 1
temp = 1
result = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 1
            
print(len(result))
result.sort()
for r in result:
    print(r)

