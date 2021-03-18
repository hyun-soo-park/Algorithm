from sys import stdin

n,k = map(int,stdin.readline().split())
coin = []
result = [0] * (k+1)
for i in range(n):
    coin.append(int(stdin.readline()))
result[0] = 1

for j in coin:
    for i in range(min(coin),k+1):
        if i-j >= 0:
            result[i] += result[i-j]

print(result[k])