# 회문2
import sys
sys.stdin = open("input.txt", "r")

def check(lst, l):
    for i in range(l//2):
        if lst[i] != lst[-1-i]:
            return False
    return True
    
for test_case in range(10):
    t = int(input())
    arr = [input() for _ in range(100)]
    arr_h = [''.join(i) for i in zip(*arr)]
    ans = 1
    flag = False
    for l in range(100, 1, -1):
        for i in range(100):
            for j in range(100-l+1):
                if check(arr[i][j:j+l],l) or check(arr_h[i][j:j+l],l):
                    ans, flag = l, True
        if flag:
            break
                
    print(f"#{t} {ans}")