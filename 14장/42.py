nums = [1,2,3]
result = []
def dfs(start,path):
    result.append(path)
    for i in range(start,len(nums)):
        dfs(i+1,path+[nums[i]])

dfs(0,[])

print(result)