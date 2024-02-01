# 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = int(1e9)
    
    def dfs(count, word, visited):
        nonlocal answer
        if word == target:
            answer = min(answer, count)
            return
        if count >= len(words):
            return
        for i in range(len(words)):
            temp = 0
            if visited[i] == True:
                continue
            for j in range(len(words[i])):
                if word[j] != words[i][j]:
                    temp += 1
            if temp == 1:
                visited[i] = True
                dfs(count+1, words[i], visited)
                visited[i] = False
        
    visited = [False] * len(words)
    dfs(0, begin, visited)
    
    return answer