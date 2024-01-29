# 수퍼바이러스
# https://softeer.ai/practice/6292
import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())
print((k*pow(p, int(n/0.1), 1000000007)) % 1000000007)