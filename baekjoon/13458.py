from sys import stdin

n = int(stdin.readline())
apply = list(map(int,stdin.readline().split()))
b,c = map(int,stdin.readline().split())

result = 0

for i in range(len(apply)):
    apply[i] -= b
    result += 1
    if apply[i] > 0:
        if apply[i] % c == 0:
            result += apply[i]//c
        else:
            result += apply[i]//c + 1

print(result)