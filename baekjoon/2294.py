from sys import stdin

n,k = map(int,stdin.readline().split())
coins = []
dp = [10001 for _ in range(k+1)]
dp[0] = 0

for i in range(n):
    coin = int(stdin.readline())
    coins.append(coin)

coins.sort()

for coin in coins:
    for i in range(coin,k+1):
        dp[i] = min(dp[i-coin]+1,dp[i])

if dp[k] > 10000:
    print(-1)
else:
    print(dp[k])