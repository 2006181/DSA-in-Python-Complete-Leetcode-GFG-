# Sum of Natural Number Cubes

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an integer  **n,** calculate the sum of series  **13 + 23 + 33 + 43 + …**  till n-th term.

 **Examples:** 

```
Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225
```

```
Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-19T14:40:08.872Z  

```py
class Solution:
    def sumOfSeries(self, n):
        def solve(n, sum):
            if n == 0:
                return sum
            return solve(n - 1, sum + n**3)

        return solve(n, 0)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1)