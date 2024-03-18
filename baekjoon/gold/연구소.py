# 연구소
# https://www.acmicpc.net/problem/14502
from itertools import combinations
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def bfs(copy_maps):
    q = deque(virus)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if copy_maps[nx][ny] == 0:
                    copy_maps[nx][ny] = 2
                    q.append([nx, ny])
    
    count = 0
    for i in range(N):
        count += copy_maps[i].count(0)
    return count


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
answer = 0

empty = []
virus = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            empty.append((i, j))
        elif maps[i][j] == 2:
            virus.append((i, j))


for combi in combinations(empty, 3):
    copy_maps = deepcopy(maps)
    for x, y in combi:
        copy_maps[x][y] = 1
    answer = max(answer, bfs(copy_maps))

print(answer)