# 삼성시의 버스 노선
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
for test_case in range(1, int(input())+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stop = []
    for _ in range(P):
        stop.append(int(input()))

    ans = [0] * P

    for i in range(N):
        ai, bi = bus[i]
        for j in range(P):
            if ai<=stop[j]<=bi:
                ans[j]+=1

    print(f'#{test_case}', end=' ')
    print(*ans)