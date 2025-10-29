import sys
input = sys.stdin.readline

# 외판원 순회 문제가 글케 중요한거임? 먼데
# 가장 적은 비용을 들이는 여행 계획 세우기
# 0은 가지 못하는 케이스

N = int(input())
W = [[] for _ in range(N)]
for i in range(N):
    W[i] = list(map(int, input().split()))

# 외판원의 순회에 필요한 최조 비용
# 최소 거리는 bfs 탐색?, dfs인가?

def dfs(start, now, value, cnt):
    global ans
    # 종료 조건
    if cnt == N:
        if W[now][start]:
            value += W[now][start]
            if ans > value:
                ans = value
        return
    if value > ans:
        return
    for i in range(N):
        if not visited[i] and W[now][i]:
            visited[i] = 1
            dfs(start, i, value + W[now][i], cnt+1)
            visited[i] = 0
    
ans = sys.maxsize
visited = [0 for _ in range(N)]
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)
            