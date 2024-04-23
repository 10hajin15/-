import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dump):
        Max_b, min_b = max(boxes), min(boxes)
        if Max_b-min_b <= 1:
            break
        boxes.remove(Max_b)
        boxes.remove(min_b)
        boxes.append(Max_b-1)
        boxes.append(min_b+1)
    print(f"#{test_case} {max(boxes) - min(boxes)}")