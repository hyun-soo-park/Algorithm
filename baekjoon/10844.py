n = int(input())

result = [[0 for _ in range(10)] for __ in range(n+1)]

for i in range(1,10):
    result[1][i] = 1

for i in range(2,n+1):
    result[i][0] = result[i-1][1]
    result[i][9] = result[i-1][8]

    for j in range(1,9):
        result[i][j] = result[i-1][j-1] + result[i-1][j+1]

print(sum(result[n])%1000000000)