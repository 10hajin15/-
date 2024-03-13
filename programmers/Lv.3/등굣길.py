# 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    maps = [[1] * m for _ in range(n)]
    
    for puddle in puddles:
        x, y = puddle
        maps[y-1][x-1] = 0
    
    for puddle in puddles:
        y, x = puddle
        if x == 1:
            for i in range(y-1, m):
                maps[0][i] = 0
        if y == 1:
            for j in range(x-1, n):
                maps[j][0] = 0  
        
    for i in range(n):
        for j in range(m):
            if i-1 < 0 or j-1 < 0:
                continue
            if maps[i][j] == 0:
                continue
            maps[i][j] = maps[i][j-1] + maps[i-1][j]

    return maps[n-1][m-1] % 1000000007 