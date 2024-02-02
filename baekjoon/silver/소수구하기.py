# 소수 구하기
# https://www.acmicpc.net/problem/1929
import math

m, n = map(int, input().split())
a = [True for _ in range(n+1)]
a[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if a[i] == True:
        j = 2
        while i*j <= n:
            a[i*j] = False
            j += 1

for i in range(m, n+1):
    if a[i]:
        print(i)