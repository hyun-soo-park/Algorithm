nums = [0,0]

def swap(x,y):
    if int(str(nums[x])+str(nums[y]))<int(str(nums[y])+str(nums[x])):
        nums[x],nums[y] = nums[y],nums[x]

nums.sort()

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        swap(i,j)

nums = list(map(str,nums))

print(nums)