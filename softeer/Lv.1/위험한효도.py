# 위험한 효도
# https://softeer.ai/practice/7368
import sys
input = sys.stdin.readline

a, b, d = map(int, input().split())
time = 0
now = 0

while now < d:
    now += a
    if now >= d:
        time += d-(now-a)
    else:
        time += a + b
now = d
while now > 0:
    now -= b
    if now <= 0:
        time += (b+now)
    else:
        time += a + b
print(time)
        