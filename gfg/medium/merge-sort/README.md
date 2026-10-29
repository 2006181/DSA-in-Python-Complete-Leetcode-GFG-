# Merge Sort

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

 **Examples:** 

```
Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: We get the sorted array after using merge sort

```

```
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: We get the sorted array after using merge sort 
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-29T19:15:01.164Z  

```py
class Solution:
    def mergeSort(self, arr, l, r):
        if l >= r:
            return

        mid = (l + r) // 2

        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid + 1, r)

        self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        left = arr[l:mid + 1]
        right = arr[mid + 1:r + 1]

        i = 0
        j = 0
        k = l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/merge-sort/1)