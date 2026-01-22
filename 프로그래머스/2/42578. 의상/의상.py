def solution(clothes):
    answer = 0
    # 1. clothes를 순회하며 해시에 넣기 (그냥 갯수만 넣기)
    d = {}
    for cloth in clothes:
        d[cloth[1]] = d.get(cloth[1], 0) + 1

    # 2. answer는 총 옷 갯수(단독) + 해시 갯수들의 총 곱 과 같음
    answer = 1
    for cnt in d.values():
            answer *= (cnt + 1)
    return answer - 1