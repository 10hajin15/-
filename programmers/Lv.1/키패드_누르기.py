# 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    answer = ''
    keypad = {
        '1': (0,0), '2': (0,1), '3': (0,2),
        '4': (1,0), '5': (1,1), '6': (1,2),
        '7': (2,0), '8': (2,1), '9': (2,2),
        '*': (3,0), '0': (3,1), '#': (3,2)
    }
    
    left_hand = keypad['*']
    right_hand = keypad['#']
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_hand = keypad[str(num)]
        elif num in [3,6,9]:
            answer += 'R'
            right_hand = keypad[str(num)]
        else:
            left_dist = abs(left_hand[0] - keypad[str(num)][0]) + abs(left_hand[1] - keypad[str(num)][1]) 
            right_dist = abs(right_hand[0] - keypad[str(num)][0]) + abs(right_hand[1] - keypad[str(num)][1]) 
            
            if left_dist < right_dist:
                answer += 'L'
                left_hand = keypad[str(num)]
            elif left_dist > right_dist:
                answer += 'R'
                right_hand = keypad[str(num)]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = keypad[str(num)]
                elif hand == 'right':
                    answer += 'R'
                    right_hand = keypad[str(num)]
    return answer
  
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"))