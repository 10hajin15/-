# 아기 상어
# https://www.acmicpc.net/problem/16236
from collections import deque

def bfs(si, sj):
    q = deque()
    v = [[0]*N for _ in range(N)]
    tlst = []
    
    q.append((si, sj))
    v[si][sj] = 1
    dist = 0

    while q:
        ci, cj = q.popleft()
        
        if dist == v[ci][cj]:
            return tlst, dist-1
        
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= shark and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                if 0 < arr[ni][nj] < shark:
                    tlst.append((ni, nj))
                    dist = v[ni][nj]
        
    return tlst, dist-1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            ci, cj = i, j
            arr[i][j] = 0

shark = 2
cnt = ans = 0

while True:
    tlst, dist = bfs(ci, cj)

    if len(tlst) == 0:
        break

    tlst.sort(key=lambda x: (x[0], x[1]))
    ci, cj = tlst[0]
    arr[ci][cj] = 0
    cnt += 1
    ans += dist

    if shark == cnt:
        cnt = 0
        shark += 1

print(ans)