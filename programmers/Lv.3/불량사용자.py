# 불량 사용자
# https://school.programmers.co.kr/learn/courses/30/lessons/64064
import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    length = len(banned_id)
    for i in range(length):
        banned_id[i] = banned_id[i].replace('*', '.')
        
    for p in permutations(user_id, length):
        p = list(p)
        flag = True
        for j in range(length):
            if re.match(banned_id[j], p[j]) and len(banned_id[j]) == len(p[j]):
                continue
            else:
                flag = False
                break
        if flag:
            if sorted(p) not in answer:
                answer.append(sorted(p))
        
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))