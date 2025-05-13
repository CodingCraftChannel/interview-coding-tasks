"""
Task: Product of Array Except Self

Given an array of integers, return a new array such that each element at index i
is the product of all the numbers in the original array except the one at i.

The solution should:
- Run in O(n) time
- Not use division
- Handle edge cases like zeros gracefully

This problem is commonly asked in interviews at companies like Uber, Amazon, and Google.
"""
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    # Compute product of elements to the left of each index
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # Multiply by product of elements to the right
    right_product = 1
    for i in reversed(range(n)):
        result[i] *= right_product
        right_product *= nums[i]

    return result

if __name__ == '__main__':
    samples = [
        ([3, 2, 1], [2, 3, 6]),
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
    ]

    for nums, expected in samples:
        result = productExceptSelf(nums)
        if result == expected:
            print(f"OK: input={nums}")
        else:
            print(f"FAILED: input={nums}, got={result}, expected={expected}")
