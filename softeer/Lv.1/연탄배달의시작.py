# 연탄 배달의 시작
# https://softeer.ai/practice/7626
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = []

for i in range(1, n):
    result.append(a[i]-a[i-1])

print(result.count(min(result)))