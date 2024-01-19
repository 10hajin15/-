# 숫자 블록
# https://school.programmers.co.kr/learn/courses/30/lessons/12923
import math

def prime_num(x):
    if x == 1:
        return 0
    prime = [1]
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0 and i <= 1e7:
            prime.append(i)
            if x // i <= 1e7:
                prime.append(x // i)
    return max(prime)

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(prime_num(i))
    return answer

print(solution(1, 10))
print(solution(11, 20))