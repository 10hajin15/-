# 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938
import math

def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    while n > 0:
        div = math.ceil(s/n)
        answer.append(div)
        s -= div
        n -= 1
    
    return sorted(answer)