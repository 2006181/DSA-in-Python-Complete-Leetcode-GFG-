class Solution:
    def armstrongNumber (self, n):
        num = n
        sum = 0
        node = len(str(num))
        while num > 0:
            ld = num % 10
            sum = sum + (ld**node)
            num = num//10
            
        return sum == n        