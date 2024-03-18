# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [input().rstrip() for _ in range(N)]

answer = int(1e9)

for i in range(N-7):
    for j in range(M-7):
        a = b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if x % 2 == 0:
                    if y % 2 == 0:
                        if maps[x][y] == 'B':
                            b += 1
                        else:
                            a += 1
                    else:
                        if maps[x][y] == 'W':
                            b += 1
                        else:
                            a += 1
                else:
                    if y % 2 == 0:
                        if maps[x][y] == 'B':
                            a += 1
                        else:
                            b += 1
                    else:
                        if maps[x][y] == 'W':
                            a += 1
                        else:
                            b += 1
        answer = min(answer, a, b)

print(answer)