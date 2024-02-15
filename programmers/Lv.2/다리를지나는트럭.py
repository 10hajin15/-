# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    cur_weight = 0
    sec = 0
    while bridge:
        cur_weight -= bridge.popleft()
        sec += 1
        if truck_weights:
            if cur_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                cur_weight += truck
            else:
                bridge.append(0)
    return sec