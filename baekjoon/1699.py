n = int(input())

find_result = [100001] * (n+1)
find_result[0] = 0
find_result[1] = 1

for i in range(2,n+1):
    for j in range(1,i):
        if j*j > i:
            break
        if find_result[i] > find_result[i-(j*j)] + 1:
            find_result[i] = find_result[i-(j*j)] + 1

print(find_result[n])