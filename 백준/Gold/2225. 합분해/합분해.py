import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 1로 다 쪼갠 다음에, K개를 더하려면 나누는 칸이 K -1 개 있으면 될듯
# k-1 위치를 바꿔가면서 -> 이게 안되는게 0도 포함이 되어야 해서 그런가
# dp[j] += dp[j-1]
# dp는 규칙성을 발견하는 것이 킥!

dp = [1] * (N + 1)

for i in range(2, K+1):
    for j in range(1, N+1):
        dp[j] += dp[j-1]

print(dp[N]%1000000000)