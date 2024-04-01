# 킹
# https://www.acmicpc.net/problem/1063

king, rock, N = map(str, input().split())

orders = {'R':(1, 0), 'L':(-1, 0), 'B':(0, -1), 'T':(0, 1), 'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1)}
row = '0ABCDEFGH'
king = (row.index(king[0]), int(king[1]))
rock = (row.index(rock[0]), int(rock[1]))

for i in range(int(N)):
    order = input()
    x, y = king
    nx, ny = x + orders[order][0], y + orders[order][1]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    if rock == (nx, ny):
        temp = (rock[0] + orders[order][0], rock[1] + orders[order][1])
        if temp[0] < 1 or temp[0] > 8 or temp[1] < 1 or temp[1] > 8:
            continue
        rock = temp
    king = (nx, ny)

print(row[king[0]]+str(king[1]))
print(row[rock[0]]+str(rock[1]))