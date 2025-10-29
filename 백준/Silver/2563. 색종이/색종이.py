import sys
input = sys.stdin.readline

# 색종이가 붙은 검은 영역의 넓이는 구하는 프로그램
N = int(input()) # 색종이 수
board = [[0 for _ in range(102)] for _ in range(102)]
cnt = 0
for _ in range(N):
    # 좌하단 좌표
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if board[i][j] == 0:
                board[i][j] = 1
                cnt += 1

print(cnt)
            
    