import sys
from collections import deque 
input = sys.stdin.readline

n, m, v = map(int, input().split())

# 간선으로 연결된 부분은 1, 아닌 부분은 0으로 표시
# 방문한 부분은 1, 아닌 부분은 0으로 표시
# 정점의 번호로 인해 n+1 * n+1 로 초기화
maps = [[0]*(n+1) for _ in range(n+1)]
visited1 = [0]*(n+1)
visited2 = [0]*(n+1)

for _ in range(m):
    i, j = map(int, input().split())
    maps[i][j] = 1
    maps[j][i] = 1

# DFS 
def dfs(v):
    print(v, end=" ")
    visited1[v]=1
    for i in range(1, n+1):
        if visited1[i]==0 and maps[v][i]==1:
            dfs(i)

# BFS
def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    while(q):
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if (visited2[i]==0 and maps[v][i]==1):
                q.append(i)
                visited2[i]=1

# 출력
dfs(v)
print()
bfs(v)
    