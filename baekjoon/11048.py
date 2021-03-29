from sys import stdin
import copy
n,m = map(int,stdin.readline().split())
graph = []
result = []

for i in range(n):
    row = list(map(int,stdin.readline().split()))
    graph.append(row)
dp = copy.deepcopy(graph)

for i in range(n):
    for j in range(m):
        if i-1>=0:
            dp[i][j] = max(dp[i-1][j]+graph[i][j],dp[i][j])
        if j-1>=0:
            dp[i][j] = max(dp[i][j-1]+graph[i][j],dp[i][j])
        if i-1>=0 and j-1>=0:
            dp[i][j] = max(dp[i-1][j-1]+graph[i][j],dp[i][j])

print(dp[n-1][m-1])