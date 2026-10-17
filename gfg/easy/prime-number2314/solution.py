class Solution:
    def isPrime(self, n):
        from math import sqrt
        if n <= 1:
            return False

        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True