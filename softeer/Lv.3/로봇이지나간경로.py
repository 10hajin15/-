# 로봇이 지나간 경로
# https://softeer.ai/practice/6275

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(h)]

mark = ['^', '<', 'v', '>']

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def findDirection(x, y):
    count = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == '#':
            direction = i
            count += 1
    return direction if count == 1 else -1

def findStart(maps):
    for x in range(h):
        for y in range(w):
            if maps[x][y] == '#':
                direction = findDirection(x, y)
                if direction != -1:
                    return x, y, direction

def navigate(x, y, direction):
    prevDir = newDir = direction
    maps[x][y] = '.'
    while True:
        while newDir == prevDir:
            print('A', end="")
            x, y = x+dx[newDir], y+dy[newDir]
            maps[x][y] = '.'
            x, y = x+dx[newDir], y+dy[newDir]
            maps[x][y] = '.'

            prevDir = newDir
            newDir = findDirection(x, y)
        if newDir == -1:
            return
        elif (newDir-prevDir) % 4 == 1:
            print('L', end="")
        elif (newDir-prevDir) % 4 == 3:
            print('R', end="")
        prevDir = newDir
            

x, y, direction = findStart(maps)
print(x+1, y+1)
print(mark[direction])
navigate(x, y, direction)