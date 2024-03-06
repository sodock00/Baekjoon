import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
people = deque()
answer = []

# 초기 배열 생성 
for i in range(1, N+1):
    people.append(i)

while(len(people)!=0):
    # 1번째부터 k-1번까지 빼서 큐의 뒤에 넣기 
    for _ in range(1, K):
        temp = people.popleft()
        people.append(temp)
    k = people.popleft()
    answer.append(k)

print(str(answer).replace('[','<').replace(']','>'))