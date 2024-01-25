# 성적 평가
# https://softeer.ai/practice/6250

# 시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# total = [0] * n

# for i in range(n):
#     temp = list(map(int, input().split()))
#     answer = []
#     for j in range(len(temp)):
#         rank = 1
#         total[j] += temp[j]
#         for k in range(len(temp)):
#             if temp[j] < temp[k]:
#                 rank += 1
#         answer.append(rank)
#     temp = []
#     print(*answer)

# answer = []
# for i in range(len(total)):
#     rank = 1
#     for j in range(len(total)):
#         if total[i] < total[j]:
#             rank += 1
#     answer.append(rank)
# print(*answer)

######### 다른 사람 풀이 #########
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

round = [list(map(int, input().split())) for _ in range(3)]
round.append([0] * n)
scores = [[0 for _ in range(n)] for _ in range(4)]

for x in range(4):
    temp = defaultdict(list)

    for y in range(n):
        if x < 3:
            round[3][y] += round[x][y]
        temp[round[x][y]].append(y)
    print('temp', temp)
    keyvalue = sorted(list(temp.keys()), reverse=True)
    rank = 1
    print('key value', keyvalue)
    for i in range(len(keyvalue)):
        t = 0
        for value in temp[keyvalue[i]]:
            scores[x][value] = rank
            t += 1
        rank += t

for score in scores:
    print(*score)