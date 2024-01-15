# 가장 많이 받은 선물
# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    answer = 0
    graph = [[0] * len(friends) for _ in range(len(friends))]
    for i in range(len(gifts)):
        a, b = gifts[i].split()
        graph[friends.index(a)][friends.index(b)] += 1
    
    for i in range(len(friends)):
        count = 0
        for j in range(len(friends)):
            if i == j:
                continue
            if graph[i][j] > graph[j][i]:
                count += 1
            if graph[i][j] == graph[j][i]:
                a = sum(graph[i])
                b = sum(graph[j])
                for k in range(len(graph)):
                    a -= graph[k][i]
                    b -= graph[k][j]
                if a > b:
                    count += 1
        answer = max(count, answer)

    return answer

print(solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]))
print(solution(["joy", "brad", "alessandro", "conan", "david"],	["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))