# 토마토
# https://www.acmicpc.net/problem/7569
from collections import deque

def bfs():
    global CNT
    q = deque(lst)

    while q:
        cz, cx, cy = q.popleft()
        for dz, dx, dy in ((1,0,0),(-1,0,0),(0,0,-1),(0,0,1),(0,-1,0),(0,1,0)):
            nz, nx, ny = cz+dz, cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<M and 0<=nz<H:
                if arr[nz][nx][ny] == 0:
                    q.append((nz, nx, ny))
                    arr[nz][nx][ny] = arr[cz][cx][cy] + 1
                    CNT -= 1
                    if CNT == 0:
                        return arr[nz][nx][ny]-1
    
    return -1

M, N, H = map(int, input().split())
arr = []

for z in range(H):
    tmp = []
    for x in range(N):
        tmp.append(list(map(int, input().split()))) 
    arr.append(tmp)

CNT = 0
lst = []
for z in range(H):
    for x in range(N):
        for y in range(M):
            if arr[z][x][y] == 0:
                CNT += 1
            elif arr[z][x][y] == 1:
                lst.append((z, x, y))
if CNT == 0:
    print(0)
else:
    print(bfs())