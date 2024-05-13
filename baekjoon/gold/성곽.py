# 성곽
# https://www.acmicpc.net/problem/2234

############# 틀림 #############

# def dfs(start):
#     global size, tmp
#     i, j = start
#     for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
#         ni, nj = i+di, j+dj
#         if 1<=ni<N*2 and 1<=nj<M*2 and arr[ni][nj]>=0 and not visited[ni][nj]:
#             visited[ni][nj] = 1
#             if arr[ni][nj] > 0:
#                 tmp += 1
#             dfs((ni, nj))
                

# M, N = map(int, input().split())
# tmp = [list(map(int, input().split())) for _ in range(N)]
# arr = [[-1]*(M*2+1)] + [[-1]+ [0]*(M*2-1) +[-1] for _ in range(N*2-1)] +  [[-1]*(M*2+1)]
# row = 0
# for i in range(1, N*2):
#     if i % 2 == 1:
#         col = 0
#         for j in range(1, M*2):
#             if j % 2 == 1:
#                 arr[i][j] = tmp[row][col]
#                 col += 1
#             else:
#                 if arr[i][j-1] >= 4 and bin(arr[i][j-1])[2:][-3] == '1':
#                     arr[i][j] = -1
#         row += 1
#     else:
#         for j in range(1, M*2):
#             if arr[i-1][j] <= 0 or (arr[i-1][j] >= 8 and bin(arr[i-1][j])[2:][-4]=='1'):
#                 arr[i][j] = -1

# cnt = size = 0
# visited = [[0]*(M*2+1) for _ in range(N*2+1)]
# for i in range(1, N*2, 2):
#     for j in range(1, M*2):
#         if arr[i][j] > 0 and not visited[i][j]:
#             visited[i][j] = 1
#             tmp = 1
#             dfs((i,j))
#             size = max(size, tmp)
#             cnt += 1

# ans = 0
# for i in range(1, N*2):
#     for j in range(1, M*2):
#         if arr[i-1][j] > 0 or arr[i][j+1] > 0 or arr[i+1][j] > 0 or arr[i][j-1] > 0 and arr[i][j] == -1:
#             visited = [[0]*(M*2+1) for _ in range(N*2+1)]
#             visited[i][j] = 1
#             tmp = 0
#             dfs((i,j))
#             ans = max(tmp, ans)

# print(cnt)
# print(size)
# print(ans)

from collections import deque

binary = [8,4,2,1]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    global group_num
    
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    area = 1

    group = []
    group.append((x, y))

    while q:
        cx, cy = q.popleft()
        wall = arr[cx][cy]
        for i in range(4):
            if wall >= binary[i]:
                wall -= binary[i]
            else:
                nx, ny = cx+dx[i], cy+dy[i]
                if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                    area += 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    group.append((nx,ny))

    for i, j in group:
        room_info[i][j].append(group_num)
        room_info[i][j].append(area)

    group_num += 1
    return area

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

visited = [[0]*N for _ in range(M)]
room_info = [[[] for _ in range(N)] for _ in range(M)]

count = 0
group_num = 0
max_area = 0
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            max_area = max(bfs(i,j), max_area)
            count += 1

maybe_max = 0
for i in range(M):
    for j in range(N):
        for d in range(4):
            if arr[i][j] >= binary[d]:
                nx, ny = i+dx[d], j+dy[d]
                arr[i][j] -= binary[d]
                if 0<=nx<M and 0<=ny<N:
                    if room_info[i][j][0] != room_info[nx][ny][0]:
                        maybe_max = max(maybe_max, room_info[i][j][1]+room_info[nx][ny][1])

print(count)
print(max_area)
print(maybe_max)