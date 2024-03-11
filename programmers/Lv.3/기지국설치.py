# 기지국 설치
# https://school.programmers.co.kr/learn/courses/30/lessons/12979
import math

def solution(n, stations, w):
    intervals = []
    total = 0
    
    if stations[0]-w-1 > 0:
        intervals.append([1, stations[0]-w-1])

    for i in range(len(stations)-1):
        start = stations[i]+w+1
        end = stations[i+1]-w-1

        if start <= end:
            intervals.append([start, end])

    if stations[-1]+w+1 <= n:
        intervals.append([stations[-1]+w+1, n])

    for interval in intervals:
        x, y = interval
        if (y-x+1) <= w*2+1:
            total += 1
        else:
            div, mod = divmod(y-x+1, w*2+1)
            total += math.ceil((y-x+1)/(w*2+1))
        
    return total