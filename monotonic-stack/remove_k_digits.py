"""
Task: Remove K Digits
Source: LeetCode 402

Description:
Given a non-negative integer num represented as a string, and an integer k,
remove k digits from the number so that the new number is the smallest possible.

Constraints:
- 1 <= num.length <= 10^5
- num consists only of digits (0-9)
- num does not contain leading zeros unless the entire number is "0"
- 0 <= k <= num.length

Example:
Input:  num = "1432219", k = 3
Output: "1219"

Approach:
We apply a Greedy + Monotonic Stack strategy to construct the smallest number.
At each step, we remove digits from the stack that are larger than the current digit,
as long as we still have digits left to remove (k > 0).
If any removals are still left after the traversal, we remove from the end of the stack.
Finally, we strip leading zeros and return the result.

Time Complexity: O(n)
Space Complexity: O(n)

Stack Evolution Insight:
- The stack only contains candidates that are smaller than the current element.
- Each element is pushed and popped at most once, making the approach efficient.
- Remaining digits (if k > 0) are removed from the end of the stack.
- Leading zeros are stripped before returning the final result.
"""
def removeKdigits(num: str, k: int) -> str:
    stack = []

    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    result = ''.join(stack).lstrip('0')

    return result if result else "0"

if __name__ == '__main__':
    samples = [
        ("1432219", 3, "1219"),
        ("10200", 1, "200"),
        ("10", 2, "0"),
        ("112", 1, "11"),
        ("9", 1, "0"),
        ("1234567890", 9, "0"),
        ("10001", 4, "0"),
        ("1000000000", 1, "0"),
        ("123456", 0, "123456"),
        ("7654321", 7, "0"),
        ("987654321", 3, "654321"),
        ("11111", 3, "11"),
        ("1" * 10**5, 99999, "1"),
    ]

    for num, k, expected in samples:
        result = removeKdigits(num, k)
        n = num[:30] + "..." if len(num) > 30 else num
        if result == expected:
            print(f"OK: num={n}, k={k}")
        else:
            print(f"FAILED: num={n}, k={k}, got={result}, expected={expected}")
