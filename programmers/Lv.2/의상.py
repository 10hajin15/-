# 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from itertools import combinations

def solution(clothes):
    answer = 1
    type = {}
    for c in clothes:
        if c[1] in type:
            type[c[1]] += 1
        else:
            type[c[1]] = 1
    
    for value in type.values():
        answer *= value + 1

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))