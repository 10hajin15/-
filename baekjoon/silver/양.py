# 양
# https://www.acmicpc.net/problem/3184

import sys
sys.setrecursionlimit(100000)

def dfs(a, b, visited):
    global w, s
    if a < 0 or a >= R or b < 0 or b >= C:
        return
    if maps[a][b] == '#':
        return
    
    if not visited[a][b]:
        visited[a][b] = True
        if maps[a][b] == 'v':
            w += 1
        elif maps[a][b] == 'o':
            s += 1
        dfs(a - 1, b, visited)
        dfs(a, b - 1, visited)
        dfs(a + 1, b, visited)
        dfs(a, b + 1, visited)

    return 

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]

wolf = 0
sheep = 0

visited = [[False] * C for _ in range(R)]

w = s = 0

for r in range(R):
    for c in range(C):
        if maps[r][c] == 'v' or maps[r][c] == 'o' and not visited[r][c]:
            dfs(r, c, visited)
            if w >= s:
                s = 0
            else:
                w = 0
            wolf += w
            sheep += s
            w = s = 0

print(sheep, wolf)