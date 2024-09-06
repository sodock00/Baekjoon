import sys
input = sys.stdin.readline

N = int(input())
dp = [-1] * (N + 5) 

dp[3] = 1
dp[5] = 1

for i in range(6, N + 1):
    if dp[i - 5] != -1:
        dp[i] = dp[i - 5] + 1
    if dp[i - 3] != -1:
        if dp[i] == -1:
            dp[i] = dp[i-3] + 1
        else:
            dp[i] = min(dp[i], dp[i - 3] + 1)

print(dp[N])