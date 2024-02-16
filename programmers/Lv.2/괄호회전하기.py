# 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502
def solution(s):
    brackets = {')':'(', ']':'[', '}':'{'}
    count = 0
    for i in range(len(s)):
        stack = []
        flag = True
        for j in range(len(s)):
            if s[j] in brackets.values():
                stack.append(s[j])
            else:
                if not stack:
                    flag = False
                    break
                a = stack.pop()
                if brackets[s[j]] != a:
                    flag = False
                    break
        if stack == [] and flag:
            count += 1
        s = s[1:] + s[0]
    return count