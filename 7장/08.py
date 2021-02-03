#https://leetcode.com/problems/trapping-rain-water/submissions/

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        maxl = 0
        resultl = 0
        maxr = 0
        resultr = 0
        mid = height.index(max(height))

        for i in range(0, mid):
            if height[i] > maxl:
                maxl = height[i]
            elif height[i] < maxl:
                resultl += maxl - height[i]

        for j in range(len(height) - 1, mid, -1):
            if height[j] > maxr:
                maxr = height[j]
            elif height[j] < maxr:
                resultr += maxr - height[j]

        return resultl + resultr