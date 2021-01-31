class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or s == s[::-1]:
            return s
        ans = []

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    ans.append(s[i:j])

        ans = sorted(ans, key=lambda x: len(x))

        return ans[-1]