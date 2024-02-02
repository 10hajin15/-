# X marks the Spot
# https://softeer.ai/practice/7703

import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b = input().split()
    a = a.upper()
    b = b.upper()
    idx = a.index('X')
    print(b[idx],end="")