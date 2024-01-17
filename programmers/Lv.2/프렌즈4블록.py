# 프렌즈 4블록
# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def check(m, n, board):
    temp = [[0 for _ in range(n)] for _ in range(m)]
    count = 0

    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] and board[i][j] != '0':
                temp[i][j], temp[i][j+1], temp[i+1][j], temp[i+1][j+1] = 1, 1, 1, 1

    for i in range(m):
        for j in range(n):
            if temp[i][j] == 1:
                count += 1
                board[i][j] = '0'
    
    if count == 0:
        return 0

    for i in range(m-2, -1, -1):
        for j in range(n):
            k = i
            while 0 <= k + 1 < m and board[k+1][j] == '0':
                k += 1
            if k != i:
                board[k][j], board[i][j] = board[i][j], board[k][j]

    return count

def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        bomb = check(m, n, board)
        if bomb == 0:
            break
        answer += bomb

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))