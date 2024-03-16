import sys
input = sys.stdin.readline

# 입력
lanson = []
K, N = map(int, input().split())
for _ in range(K):
    l = int(input())
    lanson.append(l)

# 구현
answer = []
def sol(start, end):
    if start > end:
        return 
    length = (start + end)//2
    cnt = 0
    for l in lanson:
        cnt += l//length
    # cnt < N일 경우
    if cnt < N:
        sol(start, length-1)
    # cnt > N일 경우
    elif cnt >= N:
        answer.append(length)
        sol(length+1, end)
    # cnt가 N일 경우
    elif cnt == N:
        answer.append(length)

# 출력
sol(1, max(lanson))
print(max(answer))
    