# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    count = bin(n).count('1')
    while n:
        n += 1
        if bin(n).count('1') == count:
            return n


print(solution(78))
print(solution(15))