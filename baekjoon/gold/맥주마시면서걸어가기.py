# 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205
from collections import deque

def bfs(start):
    q = deque([start])
    visited = [0] * CNT
    beer = 1000
    while q:
        x, y = q.popleft()
        if beer-(abs(end[0]-x)+abs(end[1]-y)) >= 0:
            return 'happy'
        for i in range(CNT):
            cx, cy = lst[i][0], lst[i][1]
            if not visited[i]:
                if beer-(abs(cx-x)+abs(cy-y)) >= 0:
                    visited[i] = 1
                    q.append([cx, cy])
    return 'sad'

for _ in range(int(input())):
    CNT = int(input())
    start = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(CNT)]
    end = list(map(int, input().split()))
    print(bfs(start))