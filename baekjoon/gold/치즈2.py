# 치즈2
# https://www.acmicpc.net/problem/2636
import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    visited = [[False] * M for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(a, b)])
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1
                if maps[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    maps[nx][ny] = 0

def check():
    count = 0
    for i in range(N):
        count += maps[i].count(1)
    return count

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

time = 0
count = 0
while True:
    temp = check()
    if temp:
        count = temp
        bfs(0, 0)
        time += 1
    else:
        break

print(time)
print(count)