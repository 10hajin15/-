# 스킬트리
# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for tree in skill_trees:
        flag = True
        idx = 0
        for t in tree:
            if t == skill[0]:
                idx += 1
            elif t in skill:
                if skill[idx] != t:
                    flag = False
                    break
                idx += 1
        if flag:
            answer += 1
    return answer


###### 다른 사람 풀이 ######
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer