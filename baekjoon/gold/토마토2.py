# 토마토
# https://www.acmicpc.net/problem/7576
from collections import deque

def bfs():
    global CNT
    q = deque(lst)

    while q:
        cx, cy = q.popleft()
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 0:
                    q.append((nx,ny))
                    arr[nx][ny] = arr[cx][cy] + 1
                    CNT -= 1
                    if CNT == 0:
                        return arr[nx][ny]-1

    return -1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

CNT = 0
lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            lst.append((i, j))
        elif arr[i][j] == 0:
            CNT += 1

if CNT == 0:
    print(0)
else:
    print(bfs())