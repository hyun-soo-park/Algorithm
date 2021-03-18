#https://leetcode.com/problems/k-closest-points-to-origin/submissions/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        answer = []
        for index, length in enumerate(points):
            result.append(((length[0] ** 2) + (length[1] ** 2), index))

        result = sorted(result)

        for i in range(k):
            answer.append(points[result[i][1]])

        return answer