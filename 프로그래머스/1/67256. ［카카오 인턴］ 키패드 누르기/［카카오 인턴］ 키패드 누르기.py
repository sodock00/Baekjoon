# 좌하단부터 0,0으로 생각하면 되나? 
KeyPad = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
def findKey(key):
    for i, row in enumerate(KeyPad):
        for j, val in enumerate(row):
            if key == val:
                return (i, j)
    return (-1, -1)

def solution(numbers, hand):
    L = (3, 0)
    R = (3, 2)
    C = (-1, -1)
    LL = 0
    RL = 0
    
    answer = ''
    
    for num in numbers:
        # 1, 4, 7은 L
        if num in [1, 4, 7]:
            L = findKey(num)
            print(num, 'L이동', L)
            answer += 'L'
        # 3, 6, 9는 R
        elif num in [3, 6, 9]:
            R = findKey(num)
            print(num, 'R이동', R)
            answer += 'R'
        # 2, 5, 8, 0 
        else:
            C = findKey(num)
            # L과 숫자 사이의 거리
            LL = abs(L[0]-C[0]) + abs(L[1]-C[1])
            RL = abs(R[0]-C[0]) + abs(R[1]-C[1])
            print('num', num, 'L', L, LL, 'R', R, RL)
            if LL == RL:
                if hand == "right":
                    R = C
                    answer += 'R'
                else:
                    L = C
                    answer += 'L'
            elif LL > RL:
                R = C
                answer += 'R'
            else:
                L = C
                answer += 'L'
            
            # R과 숫자 사이의 거리
            # 거리 사이 비교 -> 더 가까운 것 출력, 같다면 hand 따르기
            
    return answer