n = int(input())
stair = [0]*300
for i in range(n):
    stair[i] = int(input())

dp = [0]*300
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])
# 직전 칸에서 올라온 경우 vs. 전전 칸에서 올라온 경우
for i in range(3, n):
    dp[i] = max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2])

print(dp[n-1])