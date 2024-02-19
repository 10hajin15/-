# 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    guide = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    road = []
    x, y = 5, 5

    for d in dirs:
        nx, ny = x + guide[d][0], y + guide[d][1]
        if nx < 0 or nx > 10 or ny < 0 or ny > 10:
            continue
        if [x, y, nx, ny] not in road and [nx, ny, x, y] not in road:
            road.append([x, y, nx, ny])
        x, y = nx, ny
    return len(road)