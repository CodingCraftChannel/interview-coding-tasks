"""
Task: Ocean View
Source: LeetCode 1762 - Common in Amazon, Microsoft, and Google interviews

Description:
You're given an array `heights` representing the heights of buildings in a line,
and a string `direction` — either "EAST" or "WEST", indicating the direction the ocean faces.

A building has an ocean view if all buildings in front of it (in the direction of the ocean)
are strictly shorter. Return the list of indices of such buildings, in their original left-to-right order.

Constraints:
- 0 <= len(heights) <= 10⁵
- 0 <= heights[i] <= 10⁹
- direction ∈ {"EAST", "WEST"}

Example:
Input: heights = [3, 7, 8, 3, 6, 1], direction = "EAST"
Output: [2, 4, 5]
Explanation:
  - Building 2 (height 8) is taller than any building to its right.
  - Building 4 (height 6) is taller than building 5.
  - Building 5 (height 1) is last and has an unobstructed view.

Approach:
- Traverse the array from the ocean-facing direction.
- Track the maximum height seen so far.
- A building is added to the result if its height exceeds this maximum.
- Reverse the result if scanned right-to-left to preserve original order.

Insights:
- This is a clean one-pass O(n) solution with constant space (excluding output).
- Though no explicit stack is used, the max-tracking behavior mimics a monotonic structure.
- Efficient and ideal for real-time coding interviews.
"""
from typing import List

def oceanViewBuildings(heights: List[int], direction: str) -> List[int]:
    result = []
    max_so_far = float('-inf')

    indices = range(len(heights)) if direction == "WEST" else reversed(range(len(heights)))

    for i in indices:
        if heights[i] > max_so_far:
            result.append(i)
            max_so_far = heights[i]

    return result if direction == "WEST" else result[::-1]

if __name__ == '__main__':
    samples = [
        # Increasing heights - EAST: only last sees sunset
        ([1, 2, 3, 4], "EAST", [3]),

        # Increasing heights - WEST: all see sunset
        ([1, 2, 3, 4], "WEST", [0, 1, 2, 3]),

        # Decreasing heights - EAST: all see sunset
        ([9, 7, 5, 3, 1], "EAST", [0, 1, 2, 3, 4]),

        # Decreasing heights - WEST: only first sees sunset
        ([9, 7, 5, 3, 1], "WEST", [0]),

        # Flat skyline - only edge building can see
        ([5, 5, 5, 5], "EAST", [3]),
        ([5, 5, 5, 5], "WEST", [0]),

        # Mixed heights
        ([3, 7, 8, 3, 6, 1], "EAST", [2, 4, 5]),
        ([3, 7, 8, 3, 6, 1], "WEST", [0, 1, 2]),

        # Single building
        ([10], "EAST", [0]),
        ([10], "WEST", [0]),

        # Zigzag pattern
        ([1, 3, 2, 4, 1, 5], "EAST", [5]),
        ([1, 3, 2, 4, 1, 5], "WEST", [0, 1, 3, 5]),

        # Empty input
        ([], "EAST", []),
        ([], "WEST", []),

        # Large input: strictly increasing
        (list(range(1, 10001)), "EAST", [9999]),
        (list(range(1, 10001)), "WEST", list(range(10000))),
    ]


    for heights, direction, expected in samples:
        result = oceanViewBuildings(heights, direction)
        if len(heights) > 30:
            heights_str = f"{str(heights[:30])}..."
        else:
            heights_str = str(heights)
        if result == expected:
            print(f"OK: heights={heights_str}, direction={direction}")
        else:
            print(f"FAILED: heights={heights_str}, direction={direction}, got={result}, expected={expected}")
