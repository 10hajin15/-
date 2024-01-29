# 동계 테스트 시점 예측
# https://softeer.ai/practice/6281
import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    visited = [[False] * m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque([(a, b)])
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                else:
                    maps[nx][ny] += 1

    for j in range(n):
        for k in range(m):
            if maps[j][k] >= 3:
                maps[j][k] = 0
            elif maps[j][k] == 2:
                maps[j][k] = 1
    return

def check():
    for i in range(n):
        if maps[i].count(1):
            return True
    return False

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

time = 0
while check():
    bfs(0, 0)
    time += 1

print(time)