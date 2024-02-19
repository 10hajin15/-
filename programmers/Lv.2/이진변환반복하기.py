# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    del_zero = 0
    change_cnt = 0
    
    while True:
        del_zero += s.count('0')
        s = bin(s.count('1'))[2:]
        change_cnt += 1
        if s == '1':
            break
        
    
    return [change_cnt, del_zero]