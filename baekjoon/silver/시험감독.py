# 시험감독
# https://www.acmicpc.net/problem/13458
import sys
input = sys.stdin.readline

n = int(input())
applicants = list(map(int, input().split()))
control = list(map(int, input().split()))

ans = n
for i in range(n):
    total = applicants[i] - control[0]

    if total <= 0:
        continue

    div, mod = divmod(total, control[1])
    ans += div
    if mod:
        ans += 1

print(ans)