# 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    exp = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    info = {}
    for r in record:
        if r[0] != 'L':
            action, id, name = r.split()
            if name:
                info[id] = name
    for r in record:
        a = r.split()
        if a[0] == 'Change':
            continue
        else:
            answer.append(info[a[1]]+exp[a[0]])
    return answer