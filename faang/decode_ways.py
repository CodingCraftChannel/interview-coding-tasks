"""
Task: Decode Ways
Source: Popular Interview Question (Facebook, Amazon, Google, LeetCode #91)
        https://leetcode.com/problems/decode-ways/

Description:
Given an encoded message containing digits, determine the total number of ways
to decode it using the following mapping: 'A' → "1", 'B' → "2", ..., 'Z' → "26".

Constraints:
- The input string contains digits only.
- '0' cannot stand alone; it must be part of "10" to "26" to be valid.

Example:
Input: "111"
Output: 3
Explanation: "111" can be decoded as "AAA", "KA", or "AK".

Approach:
Use Dynamic Programming (DP) with optimized O(1) space complexity.
Track the number of decoding ways at positions i-1 and i-2 while iterating through
the input string. For each digit, combine results from single-digit and two-digit decoding
possibilities, properly handling zeros.
"""
def numDecodings(s: str) -> int:
    if not s or s[0] == "0":
        return 0

    one_step, two_steps = 1, 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != "0":
            current = one_step
        two_digits = int(s[i - 1:i + 1])
        if two_digits >= 10 and two_digits <= 26:
            current += two_steps
        two_steps, one_step = one_step, current

    return one_step

if __name__ == '__main__':
    samples = [
        # Basic examples
        ("12", 2),              # ["ab", "l"]
        ("226", 3),             # ["bbf", "bz", "vf"]
        ("111", 3),             # ["aaa", "ak", "ka"]
        # Edge cases
        ("0", 0),               # Invalid: single zero
        ("06", 0),              # Invalid: leading zero
        ("10", 1),              # ["j"]
        ("20", 1),              # ["t"]
        ("27", 1),              # ["bg"] (27 can't be decoded together)
        # Single digit
        ("8", 1),               # ["h"]
        # Long input
        ("1111111111", 89),     # Larger Fibonacci number pattern
        # Mixed valid/invalid sequences
        ("101", 1),             # ["ja"]
        ("2101", 1),            # ["u", "ja"]
        # Empty input
        ("", 0),                # No valid decoding for empty input
    ]

    for s, expected in samples:
        result = numDecodings(s)
        if result == expected:
            print(f"OK: input='{s}'")
        else:
            print(f"FAILED: input='{s}', got={result}, expected={expected}")
