import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
miro = [[] for _ in range(n)]
for i in range(n):
    miro[i] = list(map(int, input().strip()))

# 1은 이동할 수 있는 칸, 0은 이동 X
# 1,1에서 출발해서 n, m 위치로 이동할 때 지나야 하는 최소의 칸 수
# 이동은 상하좌우로 진행
# min값을 출력해야하나?

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        (x, y) = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
            else:
                continue

bfs(0, 0)
print(miro[n-1][m-1])