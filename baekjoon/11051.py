n,k = map(int,input().split())
result = 0
result_m = 1
result_d = 1
if n>k:
    for i in range(k):
        m = n-i
        d = k-i
        result_m *= m
        result_d *= d
    result = result_m//result_d
elif n==k:
    result = 1

print(result%10007)