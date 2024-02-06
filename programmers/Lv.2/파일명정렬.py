# 파일명 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/17686
def solution(files):
    temp = []
    head, number, tail = '', '', ''
    
    for file in files:       
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                
                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break
                        
                temp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    temp = sorted(temp, key=lambda x: [x[0].lower(), int(x[1])])

    return [''.join(t) for t in temp]


######### 다른 사람 풀이: 정규표현식 #########
import re
def solution(files):
    temp = [re.split("([0-9]+)", file) for file in files]
    temp = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(t) for t in temp]

import re
def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))