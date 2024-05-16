# 수의 새로운 연산

dic = {}
r_dic = {}
i, j = 1, 1
for n in range(1, 50000):
    dic[n] = (i, j)
    r_dic[(i,j)] = n
    i, j = i-1, j+1
    if i < 1:
        i, j = j, 1

for test_case in range(1, int(input())+1):
    p, q = map(int, input().split())

    pi, pj = dic[p]
    qi, qj = dic[q]
    si, sj = pi+qi, pj+qj
    ans = r_dic[(si, sj)]

    print(f"#{test_case} {ans}")