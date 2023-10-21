# 기사단원의 무기
# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def divisor(number):
    count = 0
    for i in range(1, int(number**(1/2))+1):
        if number % i == 0:
            count += 1
            if i < number//i:
                count += 1
    return count 

def solution(number, limit, power):
    weight = [0] * (number + 1)
    for i in range(1, number+1):
        count = divisor(i)
        weight[i] = power if count > limit else count    
    return sum(weight)

print(solution(10, 3, 2))