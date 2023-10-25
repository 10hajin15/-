# 대충 만든 자판
# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    key_count = {}
    for i in keymap:
        for j in range(len(i)):
            if i[j] in key_count:
                key_count[i[j]] = min(key_count[i[j]], j+1)
            else:
                key_count[i[j]] = j+1
                
    count_list = []
    for i in targets:
        count = 0  
        for j in i:
            if j not in key_count:
                count = -1
                break
            count += key_count[j]
        count_list.append(count)
    
    return count_list

print(solution(["ABACD", "BCEFP"], ["ABCD", "AABB"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
print(solution(["AA"], ["BB"]))