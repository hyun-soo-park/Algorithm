#https://leetcode.com/problems/intersection-of-two-arrays/submissions/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = collections.defaultdict(int)
        nums2_dict = collections.defaultdict(int)
        for i in nums1:
            nums1_dict[i] += 1
        for i in nums2:
            nums2_dict[i] += 1
        result = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if nums1_dict[i] > 0:
                    result.append(i)

        else:
            for i in nums1:
                if nums2_dict[i] > 0:
                    result.append(i)

        return list(set(result))