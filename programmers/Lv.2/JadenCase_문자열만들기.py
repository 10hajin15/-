# JardenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
            continue
        if s[i].isalpha() and answer:
            if answer[-1] == ' ':
                answer += s[i].upper()
                continue
        answer += s[i].lower()
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution(' ab cd'))