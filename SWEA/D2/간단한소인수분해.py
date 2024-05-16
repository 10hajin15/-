# 간단한 소인수분해
for test_case in range(1, int(input())+1):
    d = [2,3,5,7,11]
    ans = [0,0,0,0,0]

    num = int(input())
    i = 4
    while True:
        div, mod = divmod(num, d[i])

        if mod != 0:
            i -= 1
            if i < 0:
                break
        else:
            num = div
            ans[i] += 1

    print(f"#{test_case}", end=' ')
    print(*ans)