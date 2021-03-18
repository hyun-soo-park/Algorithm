from sys import stdin

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    graph = []
    for i in range(2):
        lst = list(map(int,stdin.readline().split()))
        graph.append(lst)
    result = [[0 for _ in range(n+1)] for __ in range(2)]
    result[0][1] = graph[0][0]
    result[1][1] = graph[1][0]
    for i in range(2,n+1):
        result[0][i] = max(result[1][i-1]+graph[0][i-1],max(result[0][i-2],result[1][i-2])+graph[0][i-1])
        result[1][i] = max(result[0][i-1]+graph[1][i-1],max(result[0][i-2],result[1][i-2])+graph[1][i-1])

    print(max(max(result[0]),max(result[1])))
