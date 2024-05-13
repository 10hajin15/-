# 매직 스타
# https://www.acmicpc.net/problem/3967
from collections import defaultdict
import sys

input = sys.stdin.readline



def check():
    if not (ord(star[0]) + ord(star[2]) + ord(star[5]) + ord(star[7]) == 22 + ord('A')*4):
        return False
    if not (ord(star[1]) + ord(star[2]) + ord(star[3]) + ord(star[4]) == 22 + ord('A')*4):
        return False
    if not (ord(star[0]) + ord(star[3]) + ord(star[6]) + ord(star[10]) == 22 + ord('A')*4):
        return False
    if not (ord(star[7]) + ord(star[8]) + ord(star[9]) + ord(star[10]) == 22 + ord('A')*4):
        return False
    if not (ord(star[1]) + ord(star[5]) + ord(star[8]) + ord(star[11]) == 22 + ord('A')*4):
        return False
    if not (ord(star[4]) + ord(star[6]) + ord(star[9]) + ord(star[11]) == 22 + ord('A')*4):
        return False
    return True

def dfs(n, mstar):
    global answer, flag
    if flag:
        return
    
    if n == 12:
        if check():
            flag = True
            answer = mstar[:]
        return
    
    if mstar[n] != 'x':
        dfs(n+1, mstar)
    else:
        for i in range(len(arr)):
            if not visited[arr[i]]:
                visited[arr[i]] = True
                mstar[n] = arr[i]
                dfs(n+1, mstar)
                visited[arr[i]] = False
                mstar[n] = 'x'
                
s = [list(input().rstrip()) for _ in range(5)]
star = ['' for _ in range(12)]
visited = defaultdict(bool)

idx = 0
for i in range(5):
    for j in range(9):
        if s[i][j].isalpha():
            star[idx] = s[i][j]
            idx += 1
            if s[i][j] != 'x':
                visited[s[i][j]] = True

arr = [chr(i) for i in range(ord('A'), ord('L')+1)]
answer = []
flag = False
dfs(0, star)

idx = 0
for i in range(5):
    for j in range(9):
        if s[i][j].isalpha():
            s[i][j] = answer[idx]
            idx += 1

for i in range(5):
    print(''.join(s[i]))

####### 다른 사람 풀이 #######
# arr = [list(input()) for _ in range(5)]

# def check():
#     if ans[0] + ans[2] + ans[5] + ans[7] == 26:
#         if ans[0] + ans[3] + ans[6] + ans[10] == 26:
#             if ans[1] + ans[2] + ans[3] + ans[4] == 26:
#                 if ans[1] + ans[5] + ans[8] + ans[11] == 26:
#                     if ans[4] + ans[6] + ans[9] + ans[11] == 26:
#                         if ans[7] + ans[8] + ans[9] + ans[10] == 26:
#                             return True
#     return False

# def recur(cur):
#     if cur == 12:
#         if check():
#             seq = 0
#             for i in range(5):
#                 for j in range(9):
#                     if arr[i][j] != ".":
#                         arr[i][j] = chr(ans[seq] + 64)
#                         seq += 1
#             for i in arr:
#                 print("".join(i))
#             quit()
#         return
#     if fixed[cur]:
#         recur(cur + 1)
#     else:
#         for i in range(1, 13):
#             if not visited[i]:
#                 ans[cur] = i
#                 visited[i] = True
#                 recur(cur + 1)
#                 visited[i] = False

# ans = [0 for i in range(12)]
# visited = [False for i in range(13)]
# fixed = [0 for i in range(12)]

# seq = 0
# for i in range(5):
#     for j in range(9):
#         if arr[i][j] == ".":
#             continue
#         if arr[i][j] != "x":
#             ans[seq] = ord(arr[i][j]) - 64
#             visited[ord(arr[i][j]) - 64] = True
#             fixed[seq] = True
#         seq += 1

# recur(0)