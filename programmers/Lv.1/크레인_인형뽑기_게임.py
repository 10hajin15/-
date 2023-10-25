# 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    dolls = [[] for _ in range(len(board)+1)]
    for i in range(len(board)-1, -1, -1):
        for j in range(1, len(board[i])+1):
            if board[i][j-1] != 0:
                dolls[j].append(board[i][j-1])
    count = 0
    stack = []
    for i in moves:
        if dolls[i]: stack.append(dolls[i].pop())
        if len(stack) > 1 and stack[-1] == stack[-2]:
            count += 2
            stack.pop()
            stack.pop()
    return count
  
print(solution([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2]], [1,1,2,3,2,4]))