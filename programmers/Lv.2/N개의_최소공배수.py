# N개의 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12953
import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    arr.sort()
    temp = lcm(arr[0], arr[1])
    for i in range(2, len(arr)):
        temp = lcm(temp, arr[i])

    return temp

print(solution([2,6,8,14]))
print(solution([1,2,3]))