# 연탄의 크기
# https://softeer.ai/practice/7628
import sys
import math
input = sys.stdin.readline

n = int(input())
r = list(map(int, input().split()))
r.sort()
m = r[-1]
arr = [0] * (m+1)

for i in range(2, m+1):
    j = 1
    while i * j <= m:
        if i*j in r:
            arr[i] += r.count(i*j)
        j += 1
print(max(arr))