"""
Task: Two Sum
Source: Popular FAANG Interview Question (Google, Facebook, Amazon, etc.)
        LeetCode #1 — https://leetcode.com/problems/two-sum/

Description:
Given a list of integers and a target number K, return True if any two 
distinct numbers in the list add up to K. Otherwise, return False.

This version only returns a boolean, not the indices.

Constraints:
- The same element cannot be used twice.
- The list may contain both positive and negative numbers.
- Aim for better than O(n²) time complexity.

Example:
Input:  nums = [10, 15, 3, 7],  k = 17
Output: True  # because 10 + 7 = 17

Approach:
Use a hash set to track values we've seen.
For each number in the list, check if (k - num) is already in the set.
If yes, we found a valid pair. This yields an O(n) time, O(n) space solution.
"""
from typing import List

def twoSum(nums: List[int], k: int) -> bool:
    seen = set()
    for num in nums:
        if k - num in seen:
            return True
        seen.add(num)
    return False

if __name__ == '__main__':
    samples = [
        ([10, 15, 3, 7], 17, True),
        ([1, 2, 3, 4, 5], 10, False),
        ([], 5, False),
        ([5], 10, False),
        ([8, 1, 5, 9], 10, True),
        ([4, 4], 8, True),
        ([0, -1, 2, -3, 1], -2, True),
        ([2, 4, 6, 3, 9, 11], 14, True),
        ([2, 4, 6, 3, 9, 11], 21, False),
        ([1, 2, 3, 9], 8, False),
    ]

    for nums, k, expected in samples:
        result = twoSum(nums, k)
        if result == expected:
            print(f"OK: nums={nums}, k={k}")
        else:
            print(f"FAILED: nums={nums}, k={k}, got={result}, expected={expected}")
