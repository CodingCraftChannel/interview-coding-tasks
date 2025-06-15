"""
Task: Daily Temperatures
Source: LeetCode (739)

Given a list of daily temperature readings, determine for each day
how many days you'll have to wait until a warmer temperature appears.
If no warmer temperature occurs in the future, return 0 for that day.

Constraints:
- 1 <= len(temperatures) <= 10^5
- 30 <= temperatures[i] <= 100

Approach:
- Use a monotonic decreasing stack to keep track of unresolved temperatures.
- Iterate from left to right.
- Pop from the stack while the current temperature is higher.
- For each popped index, calculate the wait time.
- Push the current index onto the stack.

Stack Evolution Insight:
- The stack holds indices of temperatures in decreasing order.
- When a warmer temperature is found, we resolve waiting days for all previous colder entries.
"""
from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack = []  # Stack of indices

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev_i = stack.pop()
            answer[prev_i] = i - prev_i
        stack.append(i)

    return answer

if __name__ == '__main__':
    samples = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),
        ([70, 71, 70, 72], [1, 2, 1, 0]),
        ([], []),
    ]

    for nums, expected in samples:
        result = dailyTemperatures(nums)
        if result == expected:
            print(f"OK: input={nums}")
        else:
            print(f"FAILED: input={nums}, got={result}, expected={expected}")
