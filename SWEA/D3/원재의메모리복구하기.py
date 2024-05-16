# 원재의 메모리 복구하기
# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

for test_case in range(1, int(input())+1):
    count = 0
    data = list(map(int, input()))
    tmp = 0
    for i in range(len(data)):
        if tmp != data[i]:
            count += 1
            tmp = data[i]
    
    print(f"#{test_case} {count}")