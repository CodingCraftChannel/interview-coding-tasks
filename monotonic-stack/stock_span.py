"""
Task: Stock Span Problem
Source: Classic algorithmic problem (not tied to a specific platform)

Description:
Given a list of daily stock prices, compute the span for each day.
The span of a stock's price on a given day is defined as the number of consecutive days 
(up to and including that day) for which the price was less than or equal to today's price.

Constraints:
- 1 ≤ len(prices) ≤ 10^5
- 1 ≤ prices[i] ≤ 10^5

Approach:
- Use a Monotonic Stack (decreasing stack) to track indices of unresolved prices.
- Iterate through the list from left to right.
- For each day:
    • Pop indices from the stack while the price at the top is less than or equal to the current price.
    • If the stack is empty, it means all previous prices are smaller → span = i + 1.
    • Otherwise, span = i - stack[-1] (distance to the last higher price).
    • Push the current index onto the stack.

Time Complexity:
- O(n), since each index is pushed and popped at most once.

Stack Evolution Insight:
- The stack holds indices of prices waiting for a higher future value.
- When a higher price is found, all smaller or equal prices are popped from the stack.
- This ensures we compute each span in constant time per day.
"""
def calculateSpan(prices):
    n = len(prices)
    span = [0] * n
    stack = []  # stack holds indices

    for i in range(n):
        # Pop indices with prices ≤ current price
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        # If stack is empty, span is full range so far
        span[i] = i + 1 if not stack else i - stack[-1]

        stack.append(i)

    return span

if __name__ == '__main__':
    samples = [
        ([100, 80, 60, 70, 60, 75, 90], [1, 1, 1, 2, 1, 4, 6]),
        ([10, 20, 30, 40, 50], [1, 2, 3, 4, 5]),
        ([50, 40, 30, 20, 10], [1, 1, 1, 1, 1]),
        ([70, 70, 70, 70], [1, 2, 3, 4]),
        ([50, 60, 50, 60, 50, 60], [1, 2, 1, 4, 1, 6]),
        ([100, 80, 60, 50, 40, 110], [1, 1, 1, 1, 1, 6]),
        ([], []),
    ]

    for prices, expected in samples:
        result = calculateSpan(prices)
        if result == expected:
            print(f"OK: input={prices}")
        else:
            print(f"FAILED: input={prices}, got={result}, expected={expected}")
