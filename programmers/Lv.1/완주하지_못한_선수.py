# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

def solution(participant, completion):
    answer = list(Counter(participant) - Counter(completion))
    return ''.join(answer)

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))