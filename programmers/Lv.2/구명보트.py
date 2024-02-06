# 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q = deque(people)
    while q:
        a = q.popleft()
        if len(q):
            b = q.pop()
            if a + b > limit:
                q.append(b)
        answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))


########### 다른 사람 풀이 ###########
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer