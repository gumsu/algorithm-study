n = int(input())
time = []
price = []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

# dp 배열 - i번째까지 누적 수익
dp = [0]*100
for i in range(n):
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]
    if dp[i + time[i]] < dp[i] + price[i]:
        dp[i + time[i]] = dp[i] + price[i]
print(dp[n])