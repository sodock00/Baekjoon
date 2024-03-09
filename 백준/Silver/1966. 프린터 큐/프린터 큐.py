import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    arr = deque()
    ans = 1
    N, M = map(int, input().split())
    arr.extend(map(int, input().split()))  # 리스트를 데크에 추가하는 방식으로 수정
    while arr:
        first = arr.popleft()  # pop() 대신 popleft() 사용
        if any(first < x for x in arr):  # 현재 문서의 중요도보다 높은 문서가 있는지 확인
            arr.append(first)  # 현재 문서를 다시 뒤로 보냄
            if M == 0:
                M = len(arr) - 1
            else:
                M -= 1
        else:
            if M == 0:
                break
            else:
                ans += 1
                M -= 1
    print(ans)

            
            