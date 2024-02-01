# 여행경로
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
def solution(tickets):
    tickets.sort()
    temp = []
    answer = []

    def dfs(count, start):
        temp.append(start)
        
        if count == len(tickets):
            answer.append(list(temp))
            return      
        for i in range(len(tickets)):
            if tickets[i][0] == start and not visited[i]:
                visited[i] = True
                dfs(count+1, tickets[i][1])
                temp.pop()
                visited[i] = False
    
    visited = [False] * len(tickets)
    
    dfs(0, "ICN")
    
    return answer[0]
