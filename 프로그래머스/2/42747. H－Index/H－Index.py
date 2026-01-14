def solution(citations):
    answer = 0
    # 1. 오름차순으로 인용 수 정렬 (0인 값들은 미리 빼둠)
    citations = [c for c in citations if c > 0]
    citations.sort()
    
    # 2. citations 앞에서부터 순회하면서 i번째에서의 인용 수와, 그 이후의 수를 비교
    h = 0 
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            h = max(h, len(citations) - i)
    # 3. 
    answer = h
    return answer