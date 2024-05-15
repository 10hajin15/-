# 로봇
# https://www.acmicpc.net/problem/13901
R, C = map(int, input().split())
arr = [[0]*C for _ in range(R)]

for _ in range(int(input())):
    br, bc = map(int, input().split())
    arr[br][bc] = -1

sr, sc = map(int, input().split())
arr[sr][sc] = 1

guide = list(map(int, input().split()))
dir = [(-1,0),(1,0),(0,-1),(0,1)]
d = 0
while True:
    flag = False
    for i in range(len(guide)):
        ni,nj = sr+dir[guide[d]-1][0], sc+dir[guide[d]-1][1]
        if 0<=ni<R and 0<=nj<C and arr[ni][nj] == 0:
            arr[ni][nj] = 1
            sr, sc = ni, nj
            flag = True
            break
        else:
            d = (d+1)%4
    if not flag: break
    
print(f"{sr} {sc}")