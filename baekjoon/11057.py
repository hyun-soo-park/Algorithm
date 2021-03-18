n = int(input())

result = [[0 for _ in range(10)] for __ in range(n+1)]

for i in range(10):
    result[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        for k in range(0,j+1):
            result[i][j] += result[i-1][k]

print(sum(result[n])%10007)