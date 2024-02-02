# Tren del Fin del Mundo
# https://softeer.ai/practice/7695
import sys
input = sys.stdin.readline

n = int(input())
info = []

for _ in range(n):
    a, b = map(int, input().split())
    info.append([a, b])
info.sort(key=lambda x:x[1])

print(*info[0])