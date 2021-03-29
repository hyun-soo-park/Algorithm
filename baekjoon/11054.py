from sys import stdin

n = int(stdin.readline())
graph = list(map(int,stdin.readline().split()))
dp = [[0 for _ in range(n)] for _ in range(2)]
result_max = 1

for i in range(n):
    for j in range(i):
        if graph[i] > graph[j]:
            dp[0][i] = max(dp[0][i],dp[0][j]+1)

for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if graph[j] < graph[i]:
            dp[1][i] = max(dp[1][i],dp[1][j]+1)

for i in range(n):
    if dp[0][i] != 0 and dp[1][i] != 0:
        result = dp[0][i] + dp[1][i] + 1
        result_max = max(result_max,result)

print(result_max)