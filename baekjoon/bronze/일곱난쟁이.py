# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

total = [int(input()) for _ in range(9)]
s = sum(total)
flag = False
for i in range(8):
    for j in range(i+1, 9):
        if s-total[i]-total[j] == 100:
            a = total[i]
            b = total[j]
            flag = True
            break
    if flag: break
total.remove(a)
total.remove(b)
total.sort()
for t in total:
    print(t)