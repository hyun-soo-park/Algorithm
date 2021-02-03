#https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = sorted(nums)
        left = 0
        right = len(nums) -1
        while left<right:
            if x[left]+x[right] == target:
                if x[left] == x[right]:
                    return [i for i,v in enumerate(nums) if v==x[left]]
                else:
                    return [nums.index(x[left]), nums.index(x[right])]
            elif x[left]+x[right] > target:
                right -= 1
            else:
                left += 1