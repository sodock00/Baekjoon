import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 각 TC에 대해 필요한 최소한의 지렁이 마리수 
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0 #방문한 곳은 0으로 변경
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny <0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

# 입력
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _  in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cnt.append(bfs(graph, i, j))
    print(len(cnt))
                
        
