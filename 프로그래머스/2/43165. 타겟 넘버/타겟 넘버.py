# 타겟 숫자가 될 경우 answer ++ 하면 됨
# 모든 경우의 수를 다 확인해봐야 하기 때문에 dfs로 풀어야 함
# 앞에서부터 두 가지 경우로 들고 가면 될듯 +, -

def solution(numbers, target):
    answer = 0
    
    def dfs(idx, sumList):
        nonlocal answer
        if idx == len(numbers):
            if sumList == target:
                answer += 1      
        else:
            curNum = numbers[idx]
            dfs(idx+1,sumList - curNum)
            dfs(idx+1,sumList + curNum)
    
    dfs(0, 0)
    return answer