#https://leetcode.com/problems/subsets/submissions/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, nums, path):
            result.append(path)
            if len(path) == len(nums):
                return

            for i in range(start, len(nums)):
                if nums[i] in path:
                    return
                dfs(start + 1, nums, path + [nums[i]])

        result = []
        dfs(0, nums, [])
        return result
