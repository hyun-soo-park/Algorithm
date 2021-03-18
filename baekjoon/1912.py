from sys import stdin

n = int(stdin.readline())

graph = list(map(int,stdin.readline().split()))

if max(graph)<0:
    print(max(graph))

else:
    get_min = [0] * (n)
    if graph[0]>0:
        get_min[0] = graph[0]

    for i in range(1,n):
        if get_min[i-1] + graph[i] < 0:
            continue
        else:
            get_min[i] = get_min[i-1] + graph[i]

    print(max(get_min))