# Reverse Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array  **a**  **rr**, you need to reverse a subarray of that array. The range of this subarray is given by indices  **l** and **r** (1-based indexing).

 **Examples:** 

```
Input: arr[] = [1, 2, 3, 4, 5, 6, 7], l = 2, r = 4
Output: [1, 4, 3, 2, 5, 6, 7]
Explanation: After reversing the elements in range 2 to 4 (2, 3, 4), modified array is 1, 4, 3, 2, 5, 6, 7.
```

```
Input: arr[] = [1, 6, 7, 4], l = 1, r = 4
Output: [4, 7, 6, 1]
Explanation: After reversing the elements in range 1 to 4 (1, 6, 7, 4), modified array is 4, 7, 6, 1.

```

 **Constraints:** 
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ l ≤ r ≤ arr.size()

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-20T12:52:14.516Z  

```py
class Solution:
    def reverseSubArray(self, arr, l, r):
        l -= 1
        r -= 1

        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return arr
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/reverse-sub-array5620/1)