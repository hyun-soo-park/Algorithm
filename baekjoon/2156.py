from sys import stdin

n = int(stdin.readline())
graph = [0]
get_max = [0] * (n+1)
for i in range(n):
    graph.append(int(stdin.readline()))

get_max[1] = graph[1]
if n>=2:
    get_max[2] = graph[1]+graph[2]

for i in range(3,n+1):
    get_max[i] = max(get_max[i-3]+graph[i-1]+graph[i],get_max[i-1],get_max[i-2]+graph[i])

print(get_max[n])