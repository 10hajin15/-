# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math
from collections import deque
def solution(progresses, speeds):
    days = deque([])
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i]) / speeds[i]))
    answer = deque([])
    temp = 1
    prev = days.popleft()
    while days:
        d = days.popleft()
        if prev >= d:
            temp += 1
        else:
            answer.append(temp)
            temp = 1
            prev = d
    answer.append(temp)
    return list(answer)