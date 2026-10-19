class Solution:
    def sumOfSeries(self, n):
        def solve(n, sum):
            if n == 0:
                return sum
            return solve(n - 1, sum + n**3)

        return solve(n, 0)