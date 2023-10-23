# 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    gym_count = [1] * (n+1)
    for i in lost:
        gym_count[i] -= 1
    for j in reserve:
        gym_count[j] += 1
    for k in range(1, len(gym_count)):
        if gym_count[k] == 2:
            if k != 1 and gym_count[k-1] == 0:
                gym_count[k-1] += 1
                gym_count[k] -= 1
            elif k != len(gym_count)-1 and gym_count[k+1] == 0:
                gym_count[k+1] += 1
                gym_count[k] -= 1
    return len(gym_count) - gym_count.count(0) - 1
  
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))