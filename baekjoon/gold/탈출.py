# 탈출
# https://www.acmicpc.net/problem/3055

########## 시간 초과 ##########
# from collections import deque

# R, C = map(int, input().split())
# arr = [list(input()) for _ in range(R)]

# CNT = time = ai = aj = 0
# wlst = deque([])
# klst = deque([])

# for i in range(R):
#     for j in range(C):
#         if arr[i][j] == 'D':
#             ai, aj = i, j
#         elif arr[i][j] == '*':
#             wlst.append((i,j))
#         elif arr[i][j] == 'S':
#             arr[i][j] = '.'
#             klst.append((i,j))
#         elif arr[i][j] == '.':
#             CNT += 1

# flag = False
# while True:
#     if flag:
#         break

#     if CNT == 0:
#         break
#     time += 1
#     wl = len(wlst)
#     kl = len(klst)

#     for _ in range(wl):
#         wi, wj = wlst.popleft()
#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni, nj = wi+di, wj+dj
#             if 0<=ni<R and 0<=nj<C and (ni,nj) not in wlst:
#                 if arr[ni][nj] == '.':
#                     arr[ni][nj] = '*'
#                     CNT -= 1
#                     wlst.append((ni, nj))
    
#     for _ in range(kl):
#         ki, kj = klst.popleft()
#         for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#             ni, nj = ki+di, kj+dj
#             if 0<=ni<R and 0<=nj<C and (ni,nj) not in klst:
#                 if arr[ni][nj] == '.':
#                     klst.append((ni, nj))
#                 if arr[ni][nj] == 'D':
#                     flag = True
#                     break
#         if flag:
#             break

# if flag:
#     print(time)
# else:
#     print('KAKTUS')


from collections import deque

def bfs():
    q = deque(lst)
    while q:
        i, j = q.popleft()
        if arr[ai][aj] == 'S':
            return v[ai][aj]-1
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = i+di, j+dj
            if 0<=ni<R and 0<=nj<C:
                if arr[i][j] == 'S' and (arr[ni][nj] == '.' or arr[ni][nj] == 'D'):
                    arr[ni][nj] = 'S'
                    v[ni][nj] = v[i][j] + 1
                    q.append((ni,nj))
                elif arr[i][j] == '*' and (arr[ni][nj] == '.' or arr[ni][nj] == 'S'):
                    arr[ni][nj] = '*'
                    q.append((ni,nj))
    return "KAKTUS"

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

lst = []
ai = aj = 0
v = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'D':
            ai, aj = i, j
        elif arr[i][j] == 'S':
            lst.append((i,j))
            v[i][j] = 1
for i in range(R):
    for j in range(C):
        if arr[i][j] == '*':
            lst.append((i,j))

print(bfs())