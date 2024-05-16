# Ladder2
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    t = int(input())
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    dist = 100*100
    ans = 0
    for j in range(1, 101):
        if arr[0][j] == 1:
            visited = [[0]*102 for _ in range(100)]
            ci, cj = 0, j
            tmp = 0
            while ci < 99:
                visited[ci][cj] = 1
                tmp += 1
                if arr[ci][cj+1] == 1 and not visited[ci][cj+1]:
                    cj += 1
                elif arr[ci][cj-1] == 1 and not visited[ci][cj-1]:
                    cj -= 1
                else:
                    ci += 1
            if tmp < dist:
                dist = tmp
                ans = j-1

    print(f"#{t} {ans}")