from sys import stdin

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    result = [0] * (n + 1)
    result[1] = 1
    if n >= 2:
        result[2] = 1
    if n >= 3:
        result[3] = 1
    for i in range(4,n+1):
        result[i] = result[i-3]+result[i-2]

    print(result[n])