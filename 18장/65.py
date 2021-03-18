#https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(bin_list, start, end, target):
            if start > end:
                return -1
            mid = (start + end) // 2
            if bin_list[mid] == target:
                return mid

            elif bin_list[mid] < target:
                return binary_search(bin_list, mid + 1, end, target)

            elif bin_list[mid] > target:
                return binary_search(bin_list, start, mid - 1, target)

        nums.sort()
        return binary_search(nums, 0, len(nums) - 1, target)