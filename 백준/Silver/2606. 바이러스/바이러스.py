import sys
input = sys.stdin.readline

# 걍 연결되어 있는 거 모두 찾으면 되는거네 dfs로 

n = int(input())
m = int(input())
node = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    i, j = map(int, input().split())
    node[i].append(j)
    node[j].append(i)

count = 0

def dfs(c):
    global count
    visited[c] = 1
    for nc in node[c]:
        if visited[nc] == 0:
            count += 1
            dfs(nc)

dfs(1)
print(count)