# 데이터 분석
# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    sort_rule = ["code", "date", "maximum", "remain"]

    for row in data:
        i = sort_rule.index(ext)
        if row[i] < val_ext:
            answer.append(row)

    return sorted(answer, key=lambda x: x[sort_rule.index(sort_by)])

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],	"date",	20300501,	"remain"))