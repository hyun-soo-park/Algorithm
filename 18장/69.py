#https://leetcode.com/problems/search-a-2d-matrix-ii/submissions/

import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if max(i) < target or min(i) > target:
                continue
            else:
                aa = bisect.bisect_left(i, target)
                if aa < len(i) and i[aa] == target:
                    return True

        return False