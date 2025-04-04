# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/

from collections import deque
import math


def calculate_flips(dq: deque):
    # Zero even pattern
    flips_zero_even = 0
    flips_one_even = 0
    for i in range(len(dq)):
        if i % 2 == 0:
            if dq[i] == "1":
                flips_zero_even += 1
            else:
                flips_one_even += 1
        elif i % 2 != 0:
            if dq[i] == "0":
                flips_zero_even += 1
            else:
                flips_one_even += 1

    return min(flips_zero_even, flips_one_even)


class SubOptimalSolution:  # O(N^2)
    def minFlips(self, s: str) -> int:

        dq = deque()
        for c in s:
            dq.append(c)

        min_flips = math.inf

        if len(s) % 2 == 0:
            return calculate_flips(dq)

        for i in range(len(s)):
            c = dq.popleft()
            dq.append(c)
            flips = calculate_flips(dq)
            min_flips = min(min_flips, flips)

        return min_flips

    class Solution:
        def minFlips(self, s: str) -> int:

            # Doubling string to apply sliding window approach
            n = len(s)
            t = s + s

            # Calculate alternating patterns
            pattern_1 = ["1" if i % 2 == 0 else "0" for i in range(len(t))]
            pattern_2 = ["0" if i % 2 == 0 else "1" for i in range(len(t))]

            # Loop over input string
            diff_1 = 0
            diff_2 = 0
            min_flips = float("inf")
            for i in range(len(t)):

                if pattern_1[i] != t[i]:
                    diff_1 += 1
                elif pattern_2[i] != t[i]:
                    diff_2 += 1

                if i >= len(s) - 1:
                    min_flips = min(min_flips, diff_1, diff_2)

                    if pattern_1[i - n + 1] != t[i - n + 1]:
                        diff_1 -= 1
                    elif pattern_2[i - n + 1] != t[i - n + 1]:
                        diff_2 -= 1

            return min_flips


