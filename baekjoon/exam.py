from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
operation = list(map(int,stdin.readline().split()))

max_number = -1000000001
min_number = 1000000001

def dfs(start,result,plus,minus,mul,div):
    global max_number
    global min_number
    if start == n:
        max_number = max(max_number,result)
        min_number = min(min_number,result)
        return

    if plus>0:
        dfs(start+1,int(result+arr[start]),plus-1,minus,mul,div)
    if minus>0:
        dfs(start+1,int(result-arr[start]),plus,minus-1,mul,div)
    if mul>0:
        dfs(start+1,int(result*arr[start]),plus,minus,mul-1,div)
    if div>0:
        if result < 0:
            dfs(start+1,-(int((-result)/arr[start])),plus,minus,mul,div-1)
        else:
            dfs(start+1,int(result/arr[start]),plus,minus,mul,div-1)

dfs(1,arr[0],operation[0],operation[1],operation[2],operation[3])

print(max_number)
print(min_number)