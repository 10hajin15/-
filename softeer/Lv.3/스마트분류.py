# 스마트 분류
# https://softeer.ai/practice/6279
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ph = list(input())

count = 0
for i in range(n):
    if ph[i] == 'P':
        for j in range(i-k, i+k+1):
            if j < 0 or j >= n:
                continue
            if ph[j] == 'H':
                count += 1
                ph[j] = 'X'
                break
print(count)