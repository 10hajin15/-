# 파리 퇴치
import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input())+1):
    ans = 0
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for k in range(i, i+M):
                s += sum(arr[k][j:j+M])
            ans = max(s, ans)

    print(f"#{test_case} {ans}")