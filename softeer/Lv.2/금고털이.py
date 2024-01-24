# 금고털이
# https://softeer.ai/practice/6288

import sys
input = sys.stdin.readline

w, n = map(int, input().split())
kind = []
for i in range(n):
    a, b = map(int, input().split())
    kind.append((a, b))

kind.sort(key=lambda x: x[1], reverse = True)

result = 0
i = 0
while w != 0:
    weight, cost = kind[i]
    if weight > w:
        result += w * cost
        break
    elif weight < w:
        result += weight * cost
        w -= weight
        i += 1
    else:
        result += weight * cost
        break
print(result)