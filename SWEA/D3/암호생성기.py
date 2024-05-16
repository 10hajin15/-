# 암호생성기

import sys
sys.stdin = open("input.txt", "r")
from collections import deque

for test_case in range(1, 11):
    T = int(input())
    arr = list(map(int, input().split()))
    q = deque(arr)
    i = 1
    while True:
        t = q.popleft()
        ti = 5 if i % 5 == 0 else i % 5
        n = t - ti
        if n <= 0:
            q.append(0)
            break
        i += 1
        q.append(n)

    print(f'#{T}', end=' ')
    print(*list(q))

        
        
