# 소수찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/12921

import math

def isPrimeNumber(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
      if(isPrimeNumber(i)):
        answer += 1
    return answer
  
print(solution(5))
