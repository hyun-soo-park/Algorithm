from sys import stdin

n,k = map(int,stdin.readline().split())
graph = [[0,0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(n):
    w,v = map(int,stdin.readline().split())
    graph.append([w,v])

for i in range(1,n+1):
    for j in range(1,k+1):
        if j>= graph[i][0]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-graph[i][0]]+graph[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])