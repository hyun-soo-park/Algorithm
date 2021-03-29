from sys import stdin
from collections import deque
import copy


def find_max(arr):
    row_max = 0
    for row in arr:
        x = max(row)
        if row_max < x:
            row_max = x
    return row_max

def next_line(arr):
    line = deque()
    while arr:
        x = arr.popleft()
        if not arr:
            line.append(x)
            break
        if x==arr[0]:
            x += arr.popleft()
            line.append(x)
        else:
            line.append(x)

    return line

def move_up(arr):
    for j in range(n):
        line = deque()
        for i in range(n):
            if arr[i][j] != 0:
                line.append(arr[i][j])
                arr[i][j] = 0
        line = next_line(line)
        for i in range(len(line)):
            arr[i][j] = line[i]
    return arr

def move_down(arr):
    for j in range(n):
        line = deque()
        for i in range(n-1, -1, -1):
            if arr[i][j] != 0:
                line.append(arr[i][j])
                arr[i][j] = 0
        line = next_line(line)
        for i in range(len(line)):
            arr[n-i-1][j] = line[i]

    return arr

def move_left(arr):
    for i in range(n):
        line = deque()
        for j in range(n):
            if arr[i][j] != 0:
                line.append(arr[i][j])
                arr[i][j] = 0
        line = next_line(line)
        for j in range(len(line)):
            arr[i][j] = line[j]
    return arr

def move_right(arr):
    for i in range(n):
        line = deque()
        for j in range(n-1,-1,-1):
            if arr[i][j] != 0:
                line.append(arr[i][j])
                arr[i][j] = 0
        line = next_line(line)
        for j in range(len(line)):
            arr[i][n-j-1] = line[j]
    return arr

def dfs(arr,count):
    if count == 5:
        global max_result
        fm = find_max(arr)
        if fm > max_result:
            max_result = fm
        return

    arr1 = copy.deepcopy(arr)
    arr2 = copy.deepcopy(arr)
    arr3 = copy.deepcopy(arr)
    arr4 = copy.deepcopy(arr)

    dfs(move_left(arr1),count+1)
    dfs(move_up(arr2),count+1)
    dfs(move_right(arr3),count+1)
    dfs(move_down(arr4),count+1)

n = int(stdin.readline())
graph = []
max_result = 2
for i in range(n):
    graph_list = list(map(int,stdin.readline().split()))
    graph.append(graph_list)

dfs(graph,0)
print(max_result)


