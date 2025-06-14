"""
Task: Contains in sorted array without *, /, or >>  
Source: Netflix interview question

Given a sorted list of integers of length N,  
determine if an element x is in the list without performing any multiplication,  
division, or bit-shift operations.  

Do this in O(log N) time.
"""
from typing import List

def contains(arr: List[int], x: int) -> bool:
    low, high = 0, len(arr) - 1

    while low <= high:
        # Compute midpoint using only + and - (no / or >>)
        mid = low
        steps = high - low
        count = 0
        while count + count + 1 <= steps:
            mid += 1
            count += 1

        # Standard binary search logic
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return False

if __name__ == '__main__':
    # Larger sample
    arr = list(range(0, 1000, 2))  # Even numbers [0, 2, ..., 998]

    samples = [
        ([], 5, False),
        ([5], 5, True),
        ([1, 3, 5, 7, 9], 1, True),
        ([1, 3, 5, 7, 9], 5, True),
        ([1, 3, 5, 7, 9], 9, True),
        ([1, 3, 5, 7, 9], 6, False),
        (arr, 0, True),
        (arr, 998, True),
        (arr, 123, False),
        (arr, 200, True),
        (arr, -1, False),
        (arr, 1001, False),
    ]

    for nums, x, expected in samples:
        result = contains(nums, x)
        if result == expected:
            print(f"OK: input={nums}, looking for={x}")
        else:
            print(f"FAILED: input={nums}, looking for={x}, got={result}, expected={expected}")
