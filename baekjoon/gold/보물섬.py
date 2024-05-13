# 보물섬
# https://www.acmicpc.net/problem/2589

from collections import deque

def bfs(start):
    global ans
    q = deque()

    x, y = start
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        i, j, dist = q.popleft()
        if dist > ans:
            ans = dist
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = i+di, j+dj
            if 0<=ni<col and 0<=nj<row and not visited[ni][nj]:
                if arr[ni][nj] == 'L':
                    visited[ni][nj] = 1
                    q.append((ni, nj, dist+1))

col, row = map(int, input().split())
arr = [list(input()) for _ in range(col)]

ans = 0

for i in range(col):
    for j in range(row):
        if arr[i][j] == 'L':
            visited = [[0] * row for _ in range(col)]
            bfs((i, j))

print(ans)