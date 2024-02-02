# 진정한 효도
# https://softeer.ai/practice/7374
import sys
from collections import defaultdict
input = sys.stdin.readline

maps = [list(map(int, input().split())) for _ in range(3)]

answer = int(1e9)
prev = 4
for i in range(3):
    temp = defaultdict(int)
    for j in range(3):
        temp[maps[i][j]] += 1
    sorted_temp = sorted(temp.items(), key= lambda x: x[1], reverse=True)
    if prev >= len(sorted_temp):
        prev = len(sorted_temp)
        if len(sorted_temp) == 1:
            answer = min(answer, 0)
        elif len(sorted_temp) == 3:
            answer = min(answer, 2)
        else:
            answer = min(answer, abs(sorted_temp[0][0]-sorted_temp[1][0]))

if answer == 0:
    print(0)
else:
    prev = 4
    for i in range(3):
        temp = defaultdict(int)
        for j in range(3):
            temp[maps[j][i]] += 1
        sorted_temp = sorted(temp.items(), key= lambda x: x[1], reverse=True)
        if prev >= len(sorted_temp):
            prev = len(sorted_temp)
            if len(sorted_temp) == 1:
                answer = min(answer, 0)
            elif len(sorted_temp) == 3:
                answer = min(answer, 2)
            else:
                answer = min(answer, abs(sorted_temp[0][0]-sorted_temp[1][0]))
    print(answer)
    