from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, maps, visited):
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 가는 곳이 유효한지 확인 
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    print(visited)
    if visited[len(maps)-1][len(maps[0])-1] == 0:
        return -1
    else:
        return visited[len(maps)-1][len(maps[0])-1]
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    answer = bfs(0, 0, maps, visited)
    return answer