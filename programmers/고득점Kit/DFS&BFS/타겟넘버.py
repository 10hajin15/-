# 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0

    def dfs(depth, sum):
        if depth == len(numbers):
            if sum == target:
                nonlocal answer
                answer += 1
            return
        dfs(depth+1, sum+numbers[depth])
        dfs(depth+1, sum-numbers[depth])

    dfs(0,0)
    return answer

print(solution([1,1,1,1,1], 3))
print(solution([4,1,2,1], 4))