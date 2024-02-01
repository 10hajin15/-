# 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    def dfs(x):
        visited[x] = True
        for i in graph[x]:
            if not visited[i]:
                dfs(i)
        return
    
    graph = [[] for _ in range(n)]
    visited = [False] * n
    answer = 0
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer