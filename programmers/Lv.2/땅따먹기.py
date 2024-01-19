# 땅따먹기
# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            m = 0
            for k in range(4):
                if j == k:
                    continue
                m = max(m, land[i-1][k])
            land[i][j] += m
    return max(land[len(land)-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))