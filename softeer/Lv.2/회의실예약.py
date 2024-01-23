# 회의실 예약
# https://softeer.ai/practice/6266

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rooms = {}
for _ in range(n):
    room = input().rstrip()
    rooms[room] = []

for _ in range(m):
    r, s, t = input().split()
    rooms[r].append((int(s), int(t)))
    rooms[r].sort()
    
rooms = sorted(rooms.items())

for x, y in enumerate(rooms):
    key, value = y
    print(f'Room {key}:')
    available = []
    temp = 9
    for i in range(len(value)):
        start, end = value[i]
        if start != temp:
            available.append(f"{format(temp, '02')}-{format(start, '02')}")
        temp = end
    if temp != 18:
        available.append(f"{format(temp, '02')}-18")
    if not available:
        print("Not available")
        if x != n-1: print("-----")
        continue
    else:
        print(f'{len(available)} available:')
        for a in available:
            print(a)
    if x != n-1:
        print('-----')