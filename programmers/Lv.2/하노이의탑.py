# 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946


def solution(n):
    def hanoi(n, start, end, wait):
        if n == 1:
            answer.append([start, end])
            return
        else:
            hanoi(n-1, start, wait, end)
            answer.append([start, end])
            hanoi(n-1, wait, end, start)

    answer = []
    hanoi(n, 1, 3, 2)
    return answer

print(solution(2))