# 숫자의 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    count = 1
    for i in range(1, n):
        j = i
        while True:
            if i == n:
                count += 1
                break
            elif i > n:
                break
            j += 1
            i += j

    return count

print(solution(15))