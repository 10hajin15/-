# 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    answer = []
    q = deque([])
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    priorities.sort()

    while q:
        idx, pri = q.popleft()
        if pri == priorities[-1]:
            answer.append(idx)
            priorities.pop()
        else:
            q.append((idx, pri))
    return answer.index(location) + 1

######## 다른 사람 풀이 ########
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer