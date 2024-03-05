# 보석 쇼핑
# https://school.programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    answer = [0, len(gems)-1]
    now = {gems[0]:1,}
    kind = set(gems)
    left, right = 0, 0
    while left < len(gems) and right < len(gems):
        if len(now) < len(kind):
            right += 1
            if right == len(gems):
                break
            now[gems[right]] = now.get(gems[right], 0) + 1
        else:
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            if now[gems[left]] == 1:
                del now[gems[left]]
            else:
                now[gems[left]] -= 1
            left += 1
    answer[0] += 1
    answer[1] += 1
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))