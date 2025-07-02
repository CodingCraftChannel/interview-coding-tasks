"""
Problem: 132 Pattern
Source: LeetCode 456 - 132 Pattern

Description:
Given an array of integers nums, return true if there exists a 132 pattern:
Find i < j < k such that nums[i] < nums[k] < nums[j].

In other words, there is a subsequence of three integers forming a "132" pattern.

Constraints:
- 1 <= nums.length <= 2 * 10⁵
- -10⁹ <= nums[i] <= 10⁹

Examples:
Input:  [1, 2, 3, 4]
Output: False

Input:  [3, 1, 4, 2]
Output: True
Explanation: The sequence 1, 4, 2 fits the 132 pattern.

Approach:
We scan the array from right to left, tracking possible '2' values using a monotonic decreasing stack.
We maintain a variable `third` which keeps track of the highest valid '2' candidate found so far.
For each element:
- If it is smaller than `third`, we found a valid 132 pattern.
- Otherwise, we pop from the stack all values smaller than the current one, updating `third`.

This strategy guarantees linear time by avoiding nested loops.

Stack Evolution Insight:
- The stack only contains candidates that are smaller than the current element.
- Each element is pushed and popped at most once, making the approach efficient.
"""
from typing import List

def find132pattern(nums: List[int]) -> bool:
    n = len(nums)
    if n < 3:
        return False

    third = float('-inf')
    stack = []

    for i in range(n - 1, -1, -1):
        if nums[i] < third:
            return True
        while stack and nums[i] > stack[-1]:
            third = stack.pop()
        stack.append(nums[i])

    return False

if __name__ == '__main__':
    samples = [
        ([1, 2, 3, 4], False),
        ([3, 1, 4, 2], True),
        ([-1, 3, 2, 0], True),
        ([1, 1, 1, 1], False),
        ([1], False),
        ([6, 12, 3, 4, 6, 11, 20], True),
        ([10, 20, 30, 5, 6, 7], False),
        ([1, 4, 0, -1, -2, -3, -1, -2], True),
        ([1, 0, 1, -4, -3], False),
        ([], False),
    ]

    for nums, expected in samples:
        result = find132pattern(nums)
        if result == expected:
            print(f"OK: input={nums}")
        else:
            print(f"FAILED: input={nums}, got={result}, expected={expected}")
