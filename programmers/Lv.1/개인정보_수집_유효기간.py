# 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    today = [int(today.split('.')[0]), (int(today.split('.')[1])-1) * 28 + int(today.split('.')[2])]

    term = {}
    for t in terms:
        t_name, t_month = t.split()
        term[t_name] = int(t_month) * 28

    answer = []
    for i in range(len(privacies)):
        p_date, p_term = privacies[i].split()
        y, m, d = map(int, p_date.split('.'))
        new_d = (m-1) * 28 + d + term[p_term]
        new_y = y
        if new_d >= 336:
            new_y += new_d // 336
            new_d %= 336
        if today[0] < new_y:
            continue
        elif today[0] > new_y:
            answer.append(i+1)
        else:
            if today[1] >= new_d:
                answer.append(i+1)
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01",	["Z 3", "D 5"],	["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
