sugar = int(input())

get = [-1] * (5001)

get[3] = 1
get[5] = 1

for i in range(6,sugar+1):
    a = -1
    b = -1
    if get[i-3] != -1:
        a = get[i-3] + 1
    if get[i-5] != -1:
        a = get[i-5] + 1

    get[i] = max(a,b)

print(get[sugar])