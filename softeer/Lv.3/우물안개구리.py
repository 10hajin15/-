# 우물 안 개구리
# https://softeer.ai/practice/6289
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
weight = list(map(int, input().split()))
relations = { x+1:[] for x in range(n)}

for i in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

count = 0
for key, value in relations.items():
    flag = True
    for i in range(len(value)):
        if weight[value[i]-1] >= weight[key-1]:
            flag = False
            break
    if flag:
        count += 1
print(count)
        