# 뱀
# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

l = int(input())
turns = deque([])
for _ in range(l):
    x, c = input().split()
    turns.append((int(x), c))

snake = deque([(0, 0)])
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0
x, y = 0, 0
while True:
    time += 1
    x, y = x + dx[direction], y + dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n or (x, y) in snake:
        break

    snake.append((x, y))

    if not board[x][y]:
        snake.popleft()
    else:
        board[x][y] = 0

    if turns and turns[0][0] == time:
        _, c = turns.popleft()
        if c == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(time)
