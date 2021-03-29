
lx = list(map(str,input()))
ly = list(map(str,input()))

dp = [[0 for _ in range(len(lx)+1)] for _ in range(len(ly)+1)]
answer = 0
for i in range(len(lx)):
    for j in range(len(ly)):
        if lx[i] == ly[j]:
            dp[j+1][i+1] = dp[j][i] + 1 
            answer = max(answer,dp[j+1][i+1])
        else:
            dp[j+1][i+1] = max(dp[j][i+1],dp[j+1][i])

print(answer)