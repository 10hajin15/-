# 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    fail = {}
    m = len(stages)
    for i in range(1, N+1):
        if m != 0:
            num = stages.count(i)
            fail[i] = num / m
            m = m - num
        else:
            fail[i] = 0
    return sorted(fail, key=lambda i: fail[i], reverse=True)

print(solution(5, [2,1,2,6,2,4,3,3]))