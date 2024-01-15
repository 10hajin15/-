# 붕대감기
# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    time = 0
    maxH = health

    for i in range(1, attacks[-1][0] + 1):
        if attacks[0][0] == i:
            time = 0
            a = attacks.pop(0)
            health -= a[1]
            if health <= 0:
                return -1
        else:
            time += 1
            health += bandage[1]
            if time == bandage[0]:
                health += bandage[2]
                time = 0
            if health > maxH:
                health = maxH

    return health

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))
