#https://leetcode.com/problems/fibonacci-number/submissions/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        fibo = [0] * (n + 2)
        fibo[1] = 1

        for i in range(2, n + 1):
            fibo[i] = fibo[i - 2] + fibo[i - 1]

        return fibo[n]