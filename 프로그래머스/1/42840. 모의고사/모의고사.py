def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    temp_ans = [0,0,0]
    
    # 각각 점수 내기
    for i in range(1, len(answers)+1):
        if p1[i%len(p1)-1] == answers[i-1]:
            temp_ans[0] += 1
        if p2[i%len(p2)-1] == answers[i-1]:
            temp_ans[1] += 1
        if p3[i%len(p3)-1] == answers[i-1]:
            temp_ans[2] += 1
    # 가장 높은 점수를 받은 사람 산출
    maxAns = max(temp_ans)
    for i in range (3):
        if temp_ans[i] >= maxAns:
            answer.append(i+1)
    answer.sort()
    return answer