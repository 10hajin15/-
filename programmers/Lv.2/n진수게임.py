# n진수 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def change(n, q):
    rev_base = ''
    if n == 0:
        return '0'
    while n > 0:
        n, rest = divmod(n, q)
        if rest == 10:
            rev_base += str('A')
        elif rest == 11:
            rev_base += str('B')
        elif rest == 12:
            rev_base += str('C')
        elif rest == 13:
            rev_base += str('D')
        elif rest == 14:
            rev_base += str('E')
        elif rest == 15:
            rev_base += str('F')
        else: rev_base += str(rest)
    return rev_base[::-1]

def solution(n, t, m, p):
    result = ''
    temp = []
    num = 0
    while len(temp) < t * m:
        for i in change(num, n):
            temp.append(i)
        num += 1
    for i in range(p-1, t*m, m):
        result += temp[i]
    return result


########## 다른 사람 풀이 ##########
DIGITS = list('0123456789ABCDEF')

def n2base(n, base):
    if n == 0:
        return DIGITS[0]
    digits = []
    while n > 0:
        digits.append(DIGITS[n % base])
        n = int(n // base)

    return ''.join(digits[::-1])


def solution(n, t, m, p):
    digits = []
    turn = 0
    while len(digits) < t * m:
        digits += list(n2base(turn, n))
        turn += 1
    return ''.join(digits[p-1::m][:t])

print(solution(2,4,2,1))