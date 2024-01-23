# 비밀 메뉴
# https://softeer.ai/practice/6269
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
secret = input().split()
user = input().split()

result = 'normal'
for i in range(n-m+1):
    if user[i:i+m] == secret:
        result = 'secret'
        break

print(result)