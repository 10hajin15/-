# 정곤이의 단조 증가하는 수

import sys
sys.stdin = open("input.txt", "r")

def check(lst):
    a = lst[0]
    b = lst[1]
    multi = str(a * b)
    t = int(multi[0])
    for i in range(1, len(multi)):
        if t > int(multi[i]):
            return False
        t = int(multi[i])
    return True


def dfs(n, start, lst):
    global ans
    if n == 2:
        if check(lst):
            ans = max(ans, lst[0]*lst[1])
        return
    
    for i in range(start, N):
        dfs(n+1, i+1, lst+[arr[i]])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = -1
    dfs(0, 0, [])

    print(f'#{test_case} {ans}')