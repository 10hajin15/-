# 상호의 배틀필드
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

for test_case in range(1, int(input())+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    N = int(input())
    data = input()
    
    guide = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

    d1 = '^v<>'
    d2 = 'UDLR'

    ci = cj = 0
    dir = ''
    for i in range(H):
        for j in range(W):
            if arr[i][j] in d1:
                ci, cj = i, j
                dir = d2[d1.index(arr[i][j])]

    for d in data:
        if d == 'S':
            ni, nj = ci+guide[dir][0], cj+guide[dir][1]
            while True:
                if ni<0 or ni>=H or nj<0 or nj>=W:
                    break
                if arr[ni][nj] == '#':
                    break
                if arr[ni][nj] == '*':
                    arr[ni][nj] = '.'
                    break
                ni, nj = ni+guide[dir][0], nj+guide[dir][1]
        else:
            dir = d
            ni, nj = ci+guide[d][0], cj+guide[d][1]
            if 0<=ni<H and 0<=nj<W:
                if arr[ni][nj] == '.':
                    arr[ci][cj] = '.'
                    ci, cj = ni, nj
            arr[ci][cj] = d1[d2.index(dir)]
    print(f'#{test_case}', end=" ")
    for i in range(H):
        print(''.join(arr[i]))
