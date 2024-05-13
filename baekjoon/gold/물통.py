# 물통
# https://acmicpc.net/problem/2251
from collections import deque

def bfs(start):
    q = deque([])
    q.append(start)
    
    def pour(a, b):
        if not visited[a][b]:
            visited[a][b] = 1
            q.append((a, b))

    while q:
        x, y = q.popleft()
        z = C - (x+y)

        if x == 0:
            answer.append(z)

        #1 A->B
        water = min(x, B-y)
        pour(x-water, y+water)
        #2 A->C
        water = min(x, C-z)
        pour(x-water, y)
        #3 B->A
        water = min(A-x, y)
        pour(x+water, y-water)
        #4 B->C
        water = min(y, C-z)
        pour(x, y-water)
        #5 C->A
        water = min(A-x, z)
        pour(x+water, y)
        #6 C->B
        water = min(B-y, z)
        pour(x, y+water)

answer = []
A, B, C = map(int, input().split())

visited = [[0] * (B+1) for _ in range(A+1)]
visited[0][0] = 1
bfs((0, 0))
print(*sorted(answer))