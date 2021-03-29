from sys import stdin

n = int(stdin.readline())
graph = list(map(int,stdin.readline().split()))
dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if graph[i] < graph[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))