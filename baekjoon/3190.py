from sys import stdin

N = int(stdin.readline())
K = int(stdin.readline())

dx = 0
dy = 1
current_x = 1
current_y = 1
tail_x = 1
tail_y = 1
tail_direction = 0
tail_direction = 1
time = 0

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
tail_direction = [[[] for _ in range(N+1)] for _ in range(N+1)]
graph[1][1] = 3 #tail
tail_direction[1][1] = [0,1]

for i in range(K):
    x,y = map(int,stdin.readline().split())
    graph[x][y] = 2 #apple

direction_count = int(stdin.readline())
direction_change = [0 for _ in range(10001)]

for i in range(direction_count):
    x,y = list(stdin.readline().split())
    direction_change[int(x)] = y

while True:
    time += 1
    now_x = current_x + dx
    now_y = current_y + dy
    flag = True
    if now_x>=1 and now_y>=1 and now_x<=N and now_y<=N:
        if graph[now_x][now_y] == 0:
            graph[now_x][now_y] = 1 #body
            graph[tail_x][tail_y] = 0
            move_x = tail_direction[tail_x][tail_y][0]
            move_y = tail_direction[tail_x][tail_y][1]
            tail_x += move_x
            tail_y += move_y
            graph[tail_x][tail_y] = 3
        elif graph[now_x][now_y] == 2:
            graph[now_x][now_y] = 1
        else:
            flag = False
    else:
        flag = False
    if not flag:
        break

    current_x = now_x
    current_y = now_y

    if direction_change[time] != 0:
        if dx==0 and dy==1:
            if direction_change[time] == 'L':
                dx = -1
                dy = 0
            else:
                dx = 1
                dy = 0
        elif dx==0 and dy==-1:
            if direction_change[time] == 'L':
                dx = 1
                dy = 0
            else:
                dx = -1
                dy = 0
        elif dx==-1 and dy==0:
            if direction_change[time] == 'L':
                dx = 0
                dy = -1
            else:
                dx = 0
                dy = 1
        elif dx==1 and dy==0:
            if direction_change[time] == 'L':
                dx = 0
                dy = 1
            else:
                dx = 0
                dy = -1
    tail_direction[current_x][current_y] = [dx,dy]

print(time)