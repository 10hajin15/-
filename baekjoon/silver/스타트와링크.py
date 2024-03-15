# 스타트와 링크
# https://www.acmicpc.net/problem/14889
import sys
from itertools import combinations

input = sys.stdin.readline

def dfs(depth, alist, blist):
    global ans
    if n == depth:
        if len(alist) == len(blist):
            asum = bsum = 0
            for i in range(n//2):
                for j in range(n//2):
                    asum += arr[alist[i]][alist[j]]
                    bsum += arr[blist[i]][blist[j]]
            ans = min(ans, abs(asum-bsum))
        return
    dfs(depth+1, alist+[depth], blist)
    dfs(depth+1, alist, blist+[depth])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)
dfs(0, [], [])
print(ans)