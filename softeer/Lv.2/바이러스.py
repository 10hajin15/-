# 바이러스
# https://softeer.ai/practice/6284
import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

print((k * pow(p, n, 1000000007)) % 1000000007)