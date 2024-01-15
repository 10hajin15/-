# 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s = list(map(int, s.split()))
    return f"{min(s)} {max(s)}"

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))