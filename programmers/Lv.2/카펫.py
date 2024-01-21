# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    total = brown + yellow
    for i in range(2, total // 2):
        if total % i == 0:
            if (i-2) * (total // i - 2) == yellow:
                return [total // i, i]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))