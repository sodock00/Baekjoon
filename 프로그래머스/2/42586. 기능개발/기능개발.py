from collections import deque
def solution(progresses, speeds):
    answer = []
    # 1. progress가 100이 되기 위해 필요한 day 수를 각 speed를 통해 미리 계산
    days = [0 for _ in range(len(progresses))]
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        days[i] = (100 - progress + speed - 1) // speed
    # 2. day를 0 인덱스부터 비교
    count = 1
    prev = days[0]
    for day in days[1:]:
        # 2-1. 맨 앞 day보다 작은 값 나올 경우 - count += 1
        if day <= prev:
            count += 1
        # 2-2. 맨 앞 day보다 큰 값 나올 결루 - ans에 count 추가하고 count 1 초기화
        else:
            answer.append(count)
            prev = day
            count = 1
            
    answer.append(count)
        
    return answer