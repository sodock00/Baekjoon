import sys
input = sys.stdin.readline 

n, k = map(int, input().split())
# value는 중복이 가능함 -> set을 사용해서 진행 (중복 제거)
value = set()
value = [ 0 for _ in range(n)]
for i in range(n):
    value[i] = int(input())

value.sort()

INF = k+1
    
# 가치의 합이 K원이 되어야 함
# 동전의 개수가 최소가 되어야 함
# 동전 중복 사용 가능

# 그림을 그려야 한다.
# dp[i][j] = i번쨰 동전을 추가했을때, j금액을 만드는 동전의 최소 갯수
# 정답은 dp[n][k]
# dp[i][j] = min(dp[i-1][j], dp[i][j-coin] + 1)

dp = [INF]*(k+1)
dp[0] = 0

for coin in value:
    for j in range(1, k+1):
        if j-coin >= 0:
            dp[j] = min(dp[j-coin]+1, dp[j])

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])

