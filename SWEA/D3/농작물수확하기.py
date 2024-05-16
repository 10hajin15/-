# 농작물 수확하기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    j1 = j2 = (N//2)
    ans = int(arr[0][j1])
    for i in range(1, N):
        if i <= N//2:
            j1, j2 = j1-1, j2+1
        else:
            j1, j2 = j1+1, j2-1
        for j in range(j1, j2+1):
            ans+=int(arr[i][j])
        
    print(f'#{test_case} {ans}')