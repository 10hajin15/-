# Sum
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    row = col = line1 = line2 = 0
    for i in range(100):
        t1 = t2 = 0
        for j in range(100):
            t1 += arr[i][j]
            t2 += arr[j][i]
            if i == j:
                line1 += arr[i][j]
            if i+j == 99:
                line2 += arr[i][j]
        row = max(row, t1)
        col = max(col, t2)
    
    ans = max(row, col, line1, line2)

    print(f'#{t} {ans}')