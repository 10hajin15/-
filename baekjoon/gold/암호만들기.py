# 암호 만들기
# https://www.acmicpc.net/problem/1759
import sys
input = sys.stdin.readline

def dfs(n, start, string):
    if n == L:
        vowel_count = sum(1 for s in string if s in vowel)
        cons_count = L - vowel_count
        if vowel_count >= 1 and cons_count >= 2:
            ans.append(string)
        return
    for i in range(start, C):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, i+1, string+alph[i])
            visited[i] = 0

L, C = map(int, input().split())
alph = sorted(list(input().split()))
vowel = 'aeiou'
ans = []
visited = [0] * C
dfs(0, 0, '')
for a in ans:
    print(a)

# 방법 1: 조합 이용
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# L, C = map(int, input().split())
# alpha = list(map(str, input().split()))
# alpha.sort()
# a = 'aeiou'

# result = list(combinations(alpha, L))

# answer = []
# for i in range(len(result)):
#     count = 0
#     for j in range(len(result[i])):
#         if result[i][j] in a:
#             count += 1
#     if count >= 1 and (L-count) >= 2:
#         answer.append(result[i])

# for ans in answer:
#     print(''.join(ans))