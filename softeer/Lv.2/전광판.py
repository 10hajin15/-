# 전광판
# https://softeer.ai/practice/6268

import sys
input = sys.stdin.readline

nums = {"0": "1110111", "1": "0010010", "2": "1011101", "3": "1011011", "4": "0111010",
       "5": "1101011", "6": "1101111", "7": "1110010", "8": "1111111", "9": "1111011"}

for i in range(int(input())):
    before, after = map(str, input().split())
    
    if len(before) != len(after):
        if len(before) > len(after):
            before, after = after, before
        before = "a" * (len(after)-len(before)) + before

    count = 0
    for j in range(len(after)-1, -1, -1):
        if before[j] == 'a':
            a = nums[after[j]]
            for k in range(7):
                if a[k] == "1":
                    count += 1
        else:
            b = nums[before[j]]
            a = nums[after[j]]
            for k in range(7):
                if b[k] != a[k]:
                    count += 1

    print(count)
        