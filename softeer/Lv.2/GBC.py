# GBC
# https://softeer.ai/practice/6270
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
standard = []
test = []
temp1, temp2 = 0, 0
result = [0]

for i in range(n):
    a, b = map(int, input().split())
    temp1 += a
    standard.append([temp1, b])

for i in range(m):
    a, b = map(int, input().split())
    temp2 += a
    test.append([temp2, b])

idx = 0
for i in range(len(test)):
    test_m = test[i][0]
    test_s = test[i][1]
    while True:
        if test_m > standard[idx][0]:
            if standard[idx][1] < test_s:
                result.append(test_s - standard[idx][1])
            idx += 1
        elif test_m < standard[idx][0]:
            if standard[idx][1] < test_s:
                result.append(test_s - standard[idx][1])
            break
        else:
            if standard[idx][1] < test_s:
                result.append(test_s - standard[idx][1])
            idx += 1
            break

print(max(result))

########## 다른 사람 풀이 ##########
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

limit_info =[0]*101

now=1

for _ in range(n):
    section, speed = map(int,input().split())
    for i in range(now, now+section):
        limit_info[i] = speed

    now = now+section

result = 0 
now = 1
for _ in range(m):
    section, speed = map(int,input().split())
    for i in range(now, now+section):
        result = max(result, speed-limit_info[i])
    now = now+section

print(result)