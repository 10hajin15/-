# 진기의 최고급 붕어빵
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

for test_case in range(1, int(input())+1):
    ans = 'Possible'

    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))

    fish = 0
    idx = 0
    for time in range(people[-1]+1):
        if time % M == 0 and time != 0:
            fish += K
        if people[idx] == time:
            if not fish:
                ans = 'Impossible'
                break
            else:
                idx += 1
                fish -= 1

    print(f"#{test_case} {ans}")