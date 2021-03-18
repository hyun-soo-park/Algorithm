from sys import stdin

def com_count(a,b):
    aa = 1
    x = 1
    for i in range(1,a+1):
        x = x*i
        aa *= b
        b -= 1
    return aa//x

n = int(stdin.readline())

for i in range(n):
    a,b = map(int,stdin.readline().split())
    print(com_count(a,b))