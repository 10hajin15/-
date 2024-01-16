# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not len(stack):
                return False
            p = stack.pop()
            if p != '(':
                return False
    return False if len(stack) else True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()()"))
print(solution("(())("))