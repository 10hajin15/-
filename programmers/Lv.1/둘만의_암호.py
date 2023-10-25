# 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    alph = list('abcdefghijklmnopqrstuvwxyz')
    for i in skip:
        alph.remove(i)
        
    for i in s:
        answer += alph[(alph.index(i) + index) % len(alph)]
    return answer

print(solution("aukks",	"wbqd",	5))

