# 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report = set(report)
    count = {id: 0 for id in id_list}
    report_id = {id: [] for id in id_list}

    for r in report:
        count[r.split()[1]] += 1
        report_id[r.split()[0]].append(r.split()[1])

    stop_user = []
    for key, value in count.items():
        if value >= k:
            stop_user.append(key)

    answer = []
    for key, value in report_id.items():
        count = 0
        for v in value:
            if v in stop_user:
                count += 1
        answer.append(count)
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))
print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"],	3))

