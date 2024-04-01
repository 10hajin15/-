# 주사위 굴리기
# https://www.acmicpc.net/problem/14499

import sys
from copy import deepcopy
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(N)]
orders = list(map(int,input().split()))
dice = [0 for _ in range(6)]
d = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]     # 동, 서, 북, 남

for order in orders:
    nx = x + d[order][0]
    ny = y + d[order][1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

    x, y = nx, ny

    if order == 1:
        temp = deepcopy(dice)
        temp[0], temp[1], temp[-1], temp[3] = dice[-1], dice[3], dice[1], dice[0]
        dice = temp
    elif order == 2:
        temp = deepcopy(dice)
        temp[0], temp[1], temp[-1], temp[3] = dice[3], dice[-1], dice[0], dice[1]
        dice = temp
    elif order == 3:
        temp = deepcopy(dice)
        temp[2], temp[3], temp[4], temp[5] = dice[3], dice[-2], dice[-1], dice[2]
        dice = temp
    else:
        temp = deepcopy(dice)
        temp[2], temp[3], temp[4], temp[5] = dice[-1], dice[2], dice[3], dice[-2]
        dice = temp
    
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[-1]
    else:
        dice[-1] = maps[nx][ny]
        maps[nx][ny] = 0
        
    print(dice[3])