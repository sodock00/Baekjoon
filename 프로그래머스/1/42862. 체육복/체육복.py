def solution(n, lost, reserve):
    r_lost = [x for x in lost if x not in reserve]
    r_reserve = [x for x in reserve if x not in lost]
    r_lost.sort()
    r_reserve.sort()
    answer = n- len(r_lost)
    
    for i in range (len(r_lost)):
        cur_num = r_lost[i]
        if cur_num-1 in r_reserve:
            answer+=1
            r_reserve.remove(cur_num-1)
        elif cur_num+1 in r_reserve: 
            answer+=1
            r_reserve.remove(cur_num+1)
            
    return answer

# 일단 확보된 수업 듣는 학생 수 : n-len(lost)
# 추가로 빌려줄 수 있는 학생 수 : lost 배열에서 앞부터 뒤를 탐색 (빌릴 수 있다면 학생 수 +1, reserve에서는 뺌)

# lost 배열을 돌면서 1) n-1이 reserve에 있는지 확인 -> 없다면 2) n+1이 있는지 확인
# 있으면 reserve에서 해당 숫자를 제거하고 학생 수 +1
# 없다면 다음 lost로 넘어감

# 문제를 제대로 읽어야 한다!!
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. -> 이걸 못봄..!!! 