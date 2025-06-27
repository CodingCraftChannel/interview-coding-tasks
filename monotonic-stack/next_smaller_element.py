"""
Task: Next Smaller Element (Monotonic Stack)
Source: Common Interview Question (Leetcode variant: 503. Next Greater Element II, reversed)

Task:
Given a list of integers, return a new list where each element is replaced
by the next smaller element to its right. If no such element exists, use -1.

Example:
Input:  [4, 8, 5, 2, 25]
Output: [2, 5, 2, -1, -1]

Constraints:
- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

Approach:
We iterate from right to left using a *monotonic increasing stack* that keeps
track of possible next smaller elements. At each step:
- We remove elements from the stack that are greater than or equal to nums[i]
- If the stack is not empty, the top of the stack is the next smaller
- Push nums[i] onto the stack

Time Complexity: O(n)
Space Complexity: O(n)

Stack Evolution Insight:
- The stack only contains candidates that are smaller than the current element.
- Each element is pushed and popped at most once, making the approach efficient.
"""
from typing import List

def nextSmallerElements(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in reversed(range(n)):
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])

    return res

if __name__ == '__main__':
    samples = [
        ([4, 8, 5, 2, 25], [2, 5, 2, -1, -1]),
        ([4, 4, 4, 4], [-1, -1, -1, -1]),
        ([9, 7, 5, 3, 1], [7, 5, 3, 1, -1]),
        ([1, 2, 3, 4, 5], [-1, -1, -1, -1, -1]),
        ([2, 1, 2, 1, 2], [1, -1, 1, -1, -1]),
        ([42], [-1]),
        ([], []),
    ]

    for nums, expected in samples:
        result = nextSmallerElements(nums)
        if result == expected:
            print(f"OK: input={nums}")
        else:
            print(f"FAILED: input={nums}, got={result}, expected={expected}")
