# 성적 평균
# https://softeer.ai/practice/6294

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
record = list(map(int, input().split()))

for i in range(k):
    a, b = map(int, input().split())
    print('{:.2f}'.format(round(sum(record[a-1:b]) / (b-a+1), 2)))