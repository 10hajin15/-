# 공원 산책
# https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    direction = {
        'E': (0, 1),
        'W': (0, -1),
        'S': (1, 0),
        'N': (-1, 0)
    }

    start = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start.append(i)
                start.append(j)
                break
        if len(start):
            break
    
    for i in range(len(routes)):
        d, step = routes[i].split()
        can = True
        for j in range(int(step)):
            if j == 0:
                nx = start[1] + direction[d][1]
                ny = start[0] + direction[d][0]
            else:
                nx += direction[d][1]
                ny += direction[d][0]
            if nx < 0 or ny < 0 or nx >= len(park[0]) or ny >= len(park):
                can = False
                break
            if park[ny][nx] == 'X':
                can = False
                break
        if can:
            start[0] = ny
            start[1] = nx
    return start

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))