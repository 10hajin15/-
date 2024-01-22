# 택배 마스터 광우
# https://softeer.ai/practice/6273

import sys
from itertools import permutations
input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().split())
rail = list(map(int, input().split()))
combi = list(permutations(rail, n))
answer = INF

for a in combi:
    weight = 0
    index = 0
    for b in range(k):
        temp = 0
        while True:
            if temp + a[index % n] > m:
                weight += temp
                break
            temp += a[index % n]
            index += 1
    answer = min(answer, weight)

print(answer)
