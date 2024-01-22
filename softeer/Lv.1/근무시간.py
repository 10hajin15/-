# 근무 시간
# https://softeer.ai/practice/6254

import sys
input = sys.stdin.readline

total = 0
for i in range(5):
    start, end = map(str, input().split())
    s_h, s_m = start.split(":")
    a = (int(s_h)*60) + int(s_m)
    e_h, e_m = end.split(":")
    b = (int(e_h)*60) + int(e_m)
    total += (b-a)

print(total)