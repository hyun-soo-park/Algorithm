#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(arr, start, end, target):
            if start > end:
                return -1
            mid = (start + end) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return bin_search(arr, start, mid - 1, target)
            else:
                return bin_search(arr, mid + 1, end, target)

        for i in range(len(numbers)):
            find = target
            find -= numbers[i]
            aa = bin_search(numbers, i + 1, len(numbers) - 1, find)
            if aa != -1:
                return [i + 1, aa + 1]
