# 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    count = 0
    x = s[0]
    x_count = 0
    not_x_count = 0
    for i in s:
        if x_count == not_x_count:
            x = i
            count += 1
            x_count = 0
            not_x_count = 0
            
        if x == i:
            x_count += 1
        else:
            not_x_count += 1
    return count
  
print(solution("abracadabra"))