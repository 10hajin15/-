# 덧칠하기
# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    count = 0
    paint = 0
    for s in section:
        if s >= paint:
            paint = s + m
            count += 1    
    return count
        
print(solution(100, 4, [2, 3, 99]))