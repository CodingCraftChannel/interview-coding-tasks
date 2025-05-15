"""
Task: First Missing Positive
Source: Stripe interview question

Given an unsorted array of integers, find the first missing positive integer
in linear time and constant space. You may modify the input array.
The array can contain duplicates and negative numbers.

Examples:
- Input: [3, 4, -1, 1] → Output: 2
- Input: [1, 2, 0]     → Output: 3
- Input: [7, 8, 9, 11] → Output: 1
"""
from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)

    # Step 1: Place each number x at index x - 1 if it's in the range [1, n]
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    # Step 2: Identify the first index i such that nums[i] != i + 1
    for i, num in enumerate(nums):
        if num != i + 1:
            return i + 1

    # Step 3: If all positions are correct, the missing number is n + 1
    return n + 1

if __name__ == '__main__':
    samples = [
        ([3, 4, -1, 1], 2),
        ([1, 2, 0], 3),
        ([7, 8, 9, 11], 1),
    ]

    for nums, expected in samples:
        result = firstMissingPositive(nums)
        if result == expected:
            print(f"OK: input={nums}")
        else:
            print(f"FAILED: input={nums}, got={result}, expected={expected}")
