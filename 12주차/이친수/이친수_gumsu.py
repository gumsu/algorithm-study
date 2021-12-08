n = int(input())

dp = [0]*91
dp[0] = 1
dp[1] = 1
for i in range(2, 90):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1])