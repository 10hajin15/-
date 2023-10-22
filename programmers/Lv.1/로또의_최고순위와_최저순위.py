# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    same_num_count = len(set(win_nums) & set(lottos))
    max_rank = 6 if (same_num_count+zero_count) < 2 else 7 - (same_num_count+zero_count)
    min_rank = 6 if same_num_count < 2 else 7 - same_num_count
    return [max_rank, min_rank]
  
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],	[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35]))