import itertools
import math

# 소수 판별 함수 
def isSoSu(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 3개의 수를 더했을 때 소수가 되는 경우의 개수 구하기
def solution(nums):
    answer = 0
    
    # 3개의 랜덤 수를 뽑아서 더하기
    nCr = itertools.combinations(nums, 3)
    # print(Sum(list(nCr))
    for i in nCr:
        sum = i[0] + i[1] + i[2]
        if isSoSu(sum):
            answer += 1

    return answer