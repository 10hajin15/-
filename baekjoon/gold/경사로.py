# 경사로
# https://www.acmicpc.net/problem/14890

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
count = 0

for i in range(N):
    flag = True
    left = maps[i][0]
    for j in range(N-1):
        right = maps[i][j+1]
        if left == right:
            left = right
            continue

        if abs(left-right) != 1:
            flag = False
            break
        
        if left < right:
            if j+1-L < 0:
                flag = False
                break
            for k in range(j, j-L, -1):
                if left != maps[i][k]:
                    flag = False
                    break
                else:
                    if visited[i][k] == 1:
                        flag = False
                        break
            if flag:
                for k in range(j, j-L, -1):
                    visited[i][k] = 1

        if right < left:
            if j+L >= N:
                flag = False
                break
            for k in range(j+1, j+L+1):
                if right != maps[i][k]:
                    flag = False
                    break
                else:
                    if visited[i][k] == 1:
                        flag = False
                        break
            if flag:
                for k in range(j+1, j+L+1):
                    visited[i][k] = 1
        if not flag:
            break
        left = right
    if flag:
        count += 1

visited = [[0] * N for _ in range(N)]
for i in range(N):
    flag = True
    left = maps[0][i]
    for j in range(N-1):
        right = maps[j+1][i]
        if left == right:
            left = right
            continue

        if abs(left-right) != 1:
            flag = False
            break
        
        if left < right:
            if j+1-L < 0:
                flag = False
                break
            for k in range(j, j-L, -1):
                if left != maps[k][i]:
                    flag = False
                    break
                else:
                    if visited[k][i] == 1:
                        flag = False
                        break
            if flag:
                for k in range(j, j-L, -1):
                    visited[k][i] = 1

        if right < left:
            if j+L >= N:
                flag = False
                break
            for k in range(j+1, j+L):
                if right != maps[k][i]:
                    flag = False
                    break
                else:
                    if visited[k][i] == 1:
                        flag = False
                        break
            if flag:
                for k in range(j+1, j+L+1):
                    visited[k][i] = 1
        left = right
    
    if flag:
        count += 1

print(count)