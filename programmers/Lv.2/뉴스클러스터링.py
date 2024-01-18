# 뉴스 클러스터링
# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    a = []
    b = []

    for i in range(1, len(str1)):
        if (str1[i-1] + str1[i]).isalpha():
            a.append(str1[i-1] + str1[i])

    for i in range(1, len(str2)):
        if (str2[i-1] + str2[i]).isalpha():
            b.append(str2[i-1] + str2[i])

    if len(a) == len(b) == 0:
        return 65536

    if len(a) > len(b):
        short, long = b, a
    else:
        short, long = a, b
    count = 0
    for i in range(len(short)):
        if short[i] in long:
            count += 1
            long.remove(short[i])
    
    return int(count / (len(a) + len(b)) * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake",	"shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
print(solution("di mi mi mi mi", "di di di go"))