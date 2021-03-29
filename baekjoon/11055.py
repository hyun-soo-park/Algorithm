from sys import stdin

n = int(stdin.readline())
graph = list(map(int,stdin.readline().split()))
dp = [graph[i] for i in range(n)]
dp[0] = graph[0]

for i in range(n):
    for j in range(i):
        if graph[i] > graph[j]:
            dp[i] = max(dp[i],dp[j]+graph[i])

print(max(dp))