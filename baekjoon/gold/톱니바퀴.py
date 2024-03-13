# 톱니바퀴
# https://www.acmicpc.net/problem/14891
import sys
from collections import deque
input = sys.stdin.readline

wheel = [deque(list(input().rstrip())) for _ in range(4)]

def change(num, dir):
    ans = [0, 0, 0, 0]
    ans[num] = dir
    a, b = num, num
    a_dir, b_dir = dir, dir
    while 0 <= a-1:
        if ans[a] == 0:
            break
        if wheel[a][6] != wheel[a-1][2]:
            ans[a-1] = -a_dir
        a -= 1
        a_dir = -a_dir
    
    while 4 > b+1:
        if ans[b] == 0:
            break
        if wheel[b][2] != wheel[b+1][6]:
            ans[b+1] = -b_dir
        b += 1
        b_dir = -b_dir
    
    return ans

for _ in range(int(input())):
    num, dir = map(int, input().split())
    num -= 1
    move = change(num, dir)
    for i in range(4):
        if move[i] == 0:
            continue
        elif move[i] == -1:
            temp = wheel[i].popleft()
            wheel[i].append(temp)
        else:
            temp = wheel[i].pop()
            wheel[i].appendleft(temp)

score = {0:1, 1:2, 2:4, 3:8}
answer = 0
for i in range(4):
    if wheel[i][0] == '1':
        answer += score[i]

print(answer)