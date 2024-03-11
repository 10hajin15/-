# 야근지수
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

# 실패 -> 시간 초과
def solution(n, works):
    answer = 0

    while n > 0:
        m = max(works)
        if m > 0:
            works[works.index(max(works))] -= 1
        n -= 1
    
    for i in works:
        answer += i ** 2
    
    return answer

# heapq 이용
import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    answer = 0
    heap = []
    
    for work in works:
        heapq.heappush(heap, -work)
    
    while n > 0:
        p = heapq.heappop(heap)
        heapq.heappush(heap, -(-p - 1))
        n -= 1
    
    for h in heap:
        answer += (-h) ** 2
    
    return answer