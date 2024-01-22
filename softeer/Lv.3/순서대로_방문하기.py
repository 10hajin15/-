# 순서대로 방문하기
# https://softeer.ai/practice/6246

import sys

input = sys.stdin.readline

def dfs(now, index):
    global count 
    if now == target[index]:
        if index == m-1:
            count += 1
            return
        else:
            index += 1

    x, y = now
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if maps[nx][ny] == 1:
            continue
        if not visited[nx][ny]:
            dfs([nx, ny], index)
    visited[x][y] = False
    return

n, m = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

target = []
for _ in range(m):
    x, y = map(int, input().split())
    target.append([x-1, y-1])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False for _ in range(n)] for _ in range(n)]
count = 0

dfs(target[0], 1)

print(count)
        