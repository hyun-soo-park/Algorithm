#https://leetcode.com/problems/permutations

from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        result = list(map(list, permutations(nums, len(nums))))

        return result
