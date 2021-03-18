from sys import stdin
import copy
n = int(stdin.readline())
price = [0]

price_e = list(map(int,(stdin.readline().split())))
price.extend(price_e)

price_max = copy.deepcopy(price)

for i in range(1,n+1):
    for j in range(1,i):
        price_max[i] = max(price_max[i],price_max[i-j]+price[j])

print(max(price_max))