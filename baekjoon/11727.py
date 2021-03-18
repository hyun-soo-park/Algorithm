n = int(input())

square = [0] * (n+1)

square[1] = 1
if n>=2:
    square[2] = 3

for i in range(3,n+1):
    square[i] = square[i-1] + 2*square[i-2]

print(square[n]%10007)