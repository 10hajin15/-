#[1차] 다트게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    num = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[num:i]) ** dart[d])
        if d == "*":
            scores[-2:] = [x * 2 for x in scores[-2:]]
        if d == "#":
            scores[-1] *= (-1)
        if not (d.isnumeric()):
            num = i + 1

    return sum(scores)
  
print(solution('1S2D*3T'))