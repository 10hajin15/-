# 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    for c in course:
        temp = defaultdict(int)
        for order in orders:
            order = sorted(list(order))
            for combi in combinations(order, c):
                temp[combi] += 1
        if temp:
            m = max(temp.values())
            if m < 2:
                continue
            for key, value in temp.items():
                if value == m:
                    answer.append(''.join(key))
    return sorted(answer)