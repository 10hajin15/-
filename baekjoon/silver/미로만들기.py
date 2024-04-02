# 미로 만들기
# https://www.acmicpc.net/problem/1347
import sys
input = sys.stdin.readline

N = int(input())
orders = list(input().rstrip())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
maps = [['#'] * 101 for _ in range(101)]
i, j, dir = 50, 50, 0
si = sj = ei = ej = 50
maps[i][j] = '.'

for order in orders:
    if order == 'L':
        dir = (dir+1) % 4
    elif order == 'R':
        dir = (dir-1) % 4
    else:
        i, j = i + di[dir], j + dj[dir]
        maps[i][j] = '.'
        si, sj, ei, ej = min(si, i), min(sj, j), max(ei, i), max(ej, j)

for i in range(si, ei+1):
    print(''.join(maps[i][sj:ej+1]))