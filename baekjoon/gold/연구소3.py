# 연구소3
# https://www.acmicpc.net/problem/17142
from collections import deque

def bfs(lst):
    v = [[0] * N for _ in range(N)]
    q = deque()

    for i, j in lst:
        q.append((i,j))
        v[i][j] = 1
    
    cnt = CNT

    while q:
        cx, cy = q.popleft()
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and v[nx][ny]==0 and arr[nx][ny]!=1:
                q.append((nx, ny))
                v[nx][ny] = v[cx][cy] + 1
                if arr[nx][ny] == 0:
                    cnt -= 1
                    if cnt == 0:
                        return v[nx][ny]-1
    
    return N*N

def dfs(n, start, lst):
    global ans
    if n == M:
        ans = min(ans, bfs(lst))
        return
    
    for i in range(start, L):
        dfs(n+1, i+1, lst+[vlst[i]])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

CNT = 0
vlst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            CNT += 1
        elif arr[i][j] == 2:
            vlst.append((i, j))
L = len(vlst)

if CNT == 0:
    ans = 0
else:
    ans = N*N
    dfs(0, 0, [])
    if ans == N*N:
        ans = -1

print(ans)