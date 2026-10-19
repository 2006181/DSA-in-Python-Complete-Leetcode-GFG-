class Solution:
    def printNos(self, n: int) -> None:
        if n == 0:
            return
        print(n, end=" ")
        self.printNos(n - 1)