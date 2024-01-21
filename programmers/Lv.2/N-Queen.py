# N-Queen
# https://school.programmers.co.kr/learn/courses/30/lessons/12952

def n_queens(i, col, n):
    count = 0
    if i == n:
        return 1

    for j in range(n):
        col[i] = j
        for k in range(i):
            if col[i] == col[k]:
                break
            if abs(col[i]-col[k]) == i-k:
                break
        else:
            count += n_queens(i+1, col, n)

    return count

def solution(n):
    col = [0] * n
    return n_queens(0, col, n)

print(solution(4))