# H-Index
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for i in range(citations[0], -1, -1):
        count = 0
        for j in range(len(citations)):
            if i <= citations[j]:
                count += 1
            else:
                break
        if count >= i:
            return i

print(solution([3, 0, 6, 1, 5]))
print(solution([0]))