# 업무 처리
# https://softeer.ai/practice/6251
import sys
from collections import deque
input = sys.stdin.readline

h, k, r = map(int, input().split())
staff = [deque() for _ in range(2**h)]
for i in range(-1, -(2**h)-1, -1):
    staff.append(deque(map(int, input().split())))

answer = 0
for day in range(r):
    for i in range(1, 2**h):
        if i == 1:
            if staff[1]:
                answer += staff[1].popleft()
        if day % 2 == 1:
            if staff[i*2]:
                staff[i].append(staff[i*2].popleft())
        elif day % 2 == 0:
            if staff[i*2+1]:
                staff[i].append(staff[i*2+1].popleft())

print(answer)

############ 다른 사람 풀이 ############
# import sys

# def work(index, depth, day):
#     global tree, H, answer
#     if depth > H:
#         return
    
#     # 말단 직원이라면 작업물을 올린다
#     if depth == H and tree[index].job:
#         now = tree[index].job.pop()
#         # 왼쪽 부하라면
#         if index % 2 == 0:
#             tree[index//2].left.append(now)
#         # 오른쪽 부하라면
#         else:
#             tree[index//2].right.append(now)
#     # 부하직원이 있다면 각 작업에 따라 작업물을 올린다
#     elif depth < H:
#         if day % 2 == 0 and tree[index].left:
#             now = tree[index].left.pop()
#             if index == 1:
#                 answer += now
#             else:
#                 if index % 2 == 0:
#                     tree[index//2].left.append(now)
#                 else:
#                     tree[index//2].right.append(now)
#         elif day % 2 == 1 and tree[index].right:
#             now = tree[index].right.pop()
#             if index == 1:
#                 answer += now
#             else:
#                 if index % 2 == 0:
#                     tree[index//2].left.append(now)
#                 else:
#                     tree[index//2].right.append(now)
#     work(index*2, depth+1, day)
#     work(index*2+1, depth+1, day)


# # 높이 초기화해주는 함수
# def init(index, depth):
#     global tree, H
#     if depth > H:
#         return
#     tree[index].depth = depth
#     init(index*2, depth+1)
#     init(index*2+1, depth+1)

# class Node:
#     def __init__(self):
#         self.depth = 0
#         self.left = []
#         self.right = []
#         self.job = []

# H, K, R = map(int, input().split())

# # 트리 생성
# tree = [Node() for _ in range(2**(H+1))]
# init(1,0)

# for i in range(2**H, 2**(H+1)):
#     data = list(map(int, input().split()))
#     # 말단 노드에 데이터 입력
#     for d in data:
#         tree[i].job.append(d)

# answer = 0

# for day in range(R):
#     work(1, 0, day)

# print(answer)