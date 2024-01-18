# 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return 0 if len(stack) else 1

print(solution("baabaa"))
print(solution("cdcd"))