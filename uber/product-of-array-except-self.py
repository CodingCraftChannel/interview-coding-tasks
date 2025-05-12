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
