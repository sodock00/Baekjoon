def score(score):
    if score == 1 or score == 0:
        return 6
    else:
        return abs(score - 7)

def solution(lottos, win_nums):
    answer = []
    minN = 0
    maxN = 0
    
    # 1. 주어진 로또 번호에서 당첨된 번호 수 세기
    win_nums.sort()
    lottos.sort()
    for i in lottos:
        if i in win_nums:
            minN += 1
        if i == 0:
            maxN += 1
    maxN += minN
    
    # 2. 최대는 당첨된 번호 수 + 0 갯수 이고, 최소는 당첨된 번호 
    answer.append(score(maxN))
    answer.append(score(minN))
    
    # 반례 ) 윈 넘버 혹은 로또 번호 중복
    return answer