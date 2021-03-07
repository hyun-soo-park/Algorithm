#https://leetcode.com/problems/combinations/
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        x = [xx + 1 for xx in range(n)]

        result = list(map(list, combinations(x, k)))

        return result