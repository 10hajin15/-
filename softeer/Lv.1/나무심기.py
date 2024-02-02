# 나무심기
# https://softeer.ai/practice/7353
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
print(max(a[0]*a[1], a[-1]*a[-2]))