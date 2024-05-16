# 조합
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n*i) % p
    return n

def power(a,b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a,b//2)**2*a)%p
    else:
        return (power(a,b//2)**2)%p

for test_case in range(1, int(input())+1):
    N, R = map(int, input().split())
    p = 1234567891

    top = factorial(N)
    bot = factorial(N-R) * factorial(R) % p

    print(f'#{test_case} {top*power(bot, p-2)%p}')

# for test_case in range(1, int(input())+1):
#     N, R = map(int, input().split())
#     p = 1234567891
#     a = b = 1
#     for i in range(R):
#         a*=N-i
#         a%=p
#     for i in range(1,R+1):
#         b*=i
#         b%=p
#     b = pow(b,-1,p)

#     print(f'#{test_case} {(a*b)%p}')