# 옹알이 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    count = 0
    for i in babbling:
        b = ''
        prev = ''
        for j in i:
            b += j
            if b in word:
                if prev == b:
                    break
                prev = b
                b = ''
        if b == '':
            count += 1
    return count
  
  
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	))