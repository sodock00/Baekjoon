import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited) #재귀로 구현
    
# 입력
N, M = map(int, input().split())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    # 간선의 양 끝 점
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(graph, i, visited)
        cnt += 1 #dfs가 한번씩 호출되고 끝나서 나온 경우가 하나의 연결된 간선 너낌
print(cnt)
