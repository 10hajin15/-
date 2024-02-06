# 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {}
    for i, a in enumerate(alp):
        dic[a] = i+1
    
    num = 27
    answer = []
    i = 0
    while i < len(msg):
        for j in range(len(msg), i, -1):
            if dic.get(msg[i:j]):
                answer.append(dic.get(msg[i:j]))
                if not dic.get(msg[i:j+1]):
                    dic[msg[i:j+1]] = num
                    num += 1
                i += j-i
    return answer