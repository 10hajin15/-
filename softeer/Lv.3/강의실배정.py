# 강의실 배정
# https://softeer.ai/practice/6291
import sys
input = sys.stdin.readline

n = int(input())

lecture = []
for _ in range(n):
    a, b = map(int, input().split())
    lecture.append([a, b])

lecture.sort(key=lambda x:x[1])

cnt = 0
now = 0
for l in lecture:
    if now <= l[0]:
        cnt +=1
        now = l[1]
print(cnt)