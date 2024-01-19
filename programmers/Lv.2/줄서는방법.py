# 줄 서는 방법
# https://school.programmers.co.kr/learn/courses/30/lessons/12936
import math

def solution(n, k):
    nums = list(range(1, n+1))
    answer = []
    while n != 0:
        fac = math.factorial(n-1)
        index = (k-1) // fac
        k = k % fac
        answer.append(nums.pop(index))
        n -= 1
    return answer