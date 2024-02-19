# 거리두기 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302#
def isValid(i,j,maps):
    case1 = [(-1,0),(1,0),(0,-1),(0,1)]
    case2 = [(-1,-1),(-1,1),(1,-1),(1,1)]
    case3 = [(-2,0),(2,0),(0,-2),(0,2)]
    
    for x in range(4):
        nx, ny = i+case1[x][0], j+case1[x][1]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if maps[nx][ny] == 'P':
            return False
    for x in range(4):
        nx, ny = i+case2[x][0], j+case2[x][1]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if maps[nx][ny] == 'P':
            if maps[nx][j] == 'X' and maps[i][ny] == 'X':
                continue
            else:
                return False
    for x in range(4):
        nx, ny = i+case3[x][0], j+case3[x][1]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if maps[nx][ny] == 'P':
            if maps[i+case1[x][0]][j+case1[x][1]] == 'X':
                continue
            else:
                return False
    return True

def solution(places):
    answer = []
    for place in places:
        for i in range(5):
            flag = True
            for j in range(5):
                if place[i][j] == 'P':
                    flag = isValid(i, j, place)
                if not flag:
                    break
            if not flag:
                break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer

###### 다른 사람 풀이 ######
from collections import deque

def bfs(p):
    start = []
    
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s])
        visited = [[0]*5 for _ in range(5)]
        distance = [[0]*5 for _ in range(5)]
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer