# 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq

def solution(operations):
    max_q = []
    min_q = []
    for oper in operations:
        a, b = oper.split(' ')
        if a == 'I':
            heapq.heappush(max_q, -int(b))
            heapq.heappush(min_q, int(b))
        else:
            if min_q:
                if b == '-1':
                    max_q.remove(-heapq.heappop(min_q))
                else:
                    min_q.remove(-heapq.heappop(max_q))
    if min_q:
        return [max(min_q),min(min_q)]
    return [0,0]

a = [1, 2, 3]
b = [3, 4]
print(a-b)