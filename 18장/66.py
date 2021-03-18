#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            a = nums.index(target)
            return a

        except:
            return -1