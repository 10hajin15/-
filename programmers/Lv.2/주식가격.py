# 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
def solution(prices):
    queue = deque(prices)
    answer = []
    while queue:
        p = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if q < p:
                break
        answer.append(sec)
    return answer