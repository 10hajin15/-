import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    temp = {}
    scores = list(map(int, input().split()))
    for score in scores:
        if temp.get(score):
            temp[score] += 1
        else:
            temp[score] = 1
    
    result = sorted(temp.items(), key = lambda x: (x[1], x[0]), reverse=True)
    print(f'#{num} {result[0][0]}')
