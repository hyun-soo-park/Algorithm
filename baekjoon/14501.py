from sys import stdin

n = int(stdin.readline())
max_pay = [0] * (n+1)
for i in range(0,n):
    if(max_pay[i]<max_pay[i-1]):
        max_pay[i] = max_pay[i-1]

    time,pay = map(int,stdin.readline().split())
    if (i+time)<=n:
        max_pay[i+time] = max(max_pay[i]+pay,max_pay[i+time])

print(max(max_pay))