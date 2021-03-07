#https://leetcode.com/problems/house-robber/submissions/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], max(nums[:i - 1]) + nums[i])

        return max(nums)