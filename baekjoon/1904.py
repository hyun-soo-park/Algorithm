n = int(input())

max_tile = [0] * (n+1)
max_tile[1] = 1
if n>=2:
    max_tile[2] = 2

for i in range(3,n+1):
    max_tile[i] = (max_tile[i-2] + max_tile[i-1])%15746

print(max_tile[n])