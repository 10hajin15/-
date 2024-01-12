# 이웃한 칸
# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    answer = 0

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = w + dx[i]
        ny = h + dy[i]
        if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board):
            continue
        if board[h][w] == board[ny][nx]:
            answer += 1

    return answer

print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]],	1,	1))
print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]],	0,	1))