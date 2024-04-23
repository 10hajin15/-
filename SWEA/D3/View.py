
import sys
sys.stdin = open("sample_input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        high = 0
        flag = True
        for j in range(i-2, i+3):
            if i == j: continue
            if buildings[i] <= buildings[j]:
                flag = False
                break
            high = max(high, buildings[j])
        if flag:
            ans += (buildings[i]-high)
    
    print(f"#{test_case} {ans}")