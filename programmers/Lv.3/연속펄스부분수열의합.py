# 연속 펄스 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/161988
def solution(sequence):
    answer = -int(1e9)
    s1, s2 = 0, 0
    s1_min, s2_min = 0, 0
    pulse = 1
    
    for i in range(len(sequence)):
        s1 += sequence[i] * pulse
        s2 += sequence[i] * (-pulse)
        
        answer = max(answer, s1-s1_min, s2-s2_min)
        
        s1_min = min(s1, s1_min)
        s2_min = min(s2, s2_min)
        
        pulse *= -1
    
    return answer