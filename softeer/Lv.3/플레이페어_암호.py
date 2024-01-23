# 플레이페어 암호
# https://softeer.ai/practice/6255
import sys
input = sys.stdin.readline

message = list(input().rstrip())
key = list(dict.fromkeys(list(input().rstrip())))

alp = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
secret = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        if key:
            secret[i][j] = key[0]
            alp.remove(key[0])
            key.pop(0)
        else:
            secret[i][j] = alp[0]
            alp.pop(0)

m = []

while message:
    if len(message) == 1:
        m.append(message[0]+'X')
        break
    else:
        if message[0] != message[1]:
            m.append(message[0]+message[1])
            message.pop(0)
            message.pop(0)
        else:
            if message[0] != 'X':
                m.append(message[0]+'X')
            else:
                m.append(message[0]+'Q')
            message.pop(0)

result = ''
for i in range(len(m)):
    a, b = m[i]
    ai = []
    bi = []
    for j in range(5):
        for k in range(5):
            if secret[j][k] == a:
                ai.append(j)
                ai.append(k)
            if secret[j][k] == b:
                bi.append(j)
                bi.append(k)
    if ai[0] == bi[0]:
        result += secret[ai[0]][(ai[1]+1)%5]
        result += secret[bi[0]][(bi[1]+1)%5]
    elif ai[1] == bi[1]:
        result += secret[(ai[0]+1)%5][ai[1]]
        result += secret[(bi[0]+1)%5][bi[1]]
    else:
        result += secret[ai[0]][bi[1]]
        result += secret[bi[0]][ai[1]]
print(result)