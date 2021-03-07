#https://leetcode.com/problems/combination-sum/submissions/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(findsum, start, candidates, path):
            if findsum == 0:
                result.append(path)
                return
            elif findsum < 0:
                return

            for i in range(start, len(candidates)):
                dfs(findsum - candidates[i], i, candidates, path + [candidates[i]])

        result = []
        dfs(target, 0, candidates, [])

        return result