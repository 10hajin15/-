# 캐시
# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()         # deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
        else:
            answer += 5
        q.append(city)
        if len(q) > cacheSize:
            q.popleft()
    return answer