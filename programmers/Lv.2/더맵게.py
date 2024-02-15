# 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        mix = m1 + (m2 * 2)
        heapq.heappush(scoville, mix)
        count += 1
    return count