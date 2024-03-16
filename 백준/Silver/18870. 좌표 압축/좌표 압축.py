import sys
input = sys.stdin.readline

# 입력
N = int(input())
coordinates = list(map(int, input().split()))

# 구현
ans = []
coor_idx = list(set(coordinates))
coor_idx.sort()

dic = {coor_idx[i] : i for i in range(len(coor_idx)) }

# 출력
for i in coordinates:
    print(dic[i], end=" ")
