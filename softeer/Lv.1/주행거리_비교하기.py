# 주행거리 비교하기
# https://softeer.ai/practice/6253

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("same")
