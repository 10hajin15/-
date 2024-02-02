# 암호 만들기
# https://www.acmicpc.net/problem/1759
import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
a = 'aeiou'

result = list(combinations(alpha, L))

answer = []
for i in range(len(result)):
    count = 0
    for j in range(len(result[i])):
        if result[i][j] in a:
            count += 1
    if count >= 1 and (L-count) >= 2:
        answer.append(result[i])

for ans in answer:
    print(''.join(ans))