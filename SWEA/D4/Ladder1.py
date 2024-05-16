# Ladder1
import sys
sys.stdin = open("input.txt", "r")
    
for _ in range(10):
    t = int(input())
    n = 100
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    
    ci = 99
    for j in range(100):
        if arr[ci][j] == 2:
            cj = j
    
    while ci > 0:
        arr[ci][cj] = 0
        if arr[ci][cj-1] == 1:
            cj -= 1
        elif arr[ci][cj+1] == 1:
            cj += 1
        else:
            ci -= 1

    print(f"#{t} {cj-1}")