class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(start, path, result):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(start, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j, result)

        result = []
        dfs(0, "", result)

        return result