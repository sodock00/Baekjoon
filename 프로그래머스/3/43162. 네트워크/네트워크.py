def dfs(v, visited, graph, n):
    visited[v] = 1
    # 인접한 노드들 탐색
    for i in range(n):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i, visited, graph, n)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(i, visited, computers, n)
    
    return answer