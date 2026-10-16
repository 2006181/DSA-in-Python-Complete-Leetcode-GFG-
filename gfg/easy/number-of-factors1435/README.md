# Number of factors

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Find the number of factors for a given integer  **n**.

  **Examples:** 

```
Input: n = 5
Output: 2
Explanation: 5 has 2 factors 1 and 5
```

```
Input: n = 25
Output: 3
Explanation: 25 has 3 factors 1, 5, 25 
```

 **Constraints:** 
1 ≤ n ≤ 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-16T07:20:59.686Z  

```py
class Solution:
    def countFactors (self, n):
        count = 0

        i = 1
        while i * i <= n:
            if n % i == 0:
                count += 1

                if i != n // i:
                    count += 1

            i += 1

        return count
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/number-of-factors1435/1)