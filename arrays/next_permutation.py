# https://leetcode.com/problems/next-permutation/description/

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Find first index where right < right + 1
        # For example:
        # 123 -> p1 = 1
        # 231 -> p1 = 0
        p1 = len(nums) - 2
        while nums[p1] >= nums[p1 + 1] and p1 >= 0:
            p1 -= 1

        # Reverse nums if p1 == -1
        if p1 == -1:
            nums.reverse()

            return

            # Find index smaller than p1 (if any) on the right side
        # We need to swap them to ensure that we are finding the next permutation
        p2 = len(nums) - 1
        while nums[p2] <= nums[p1]:
            p2 -= 1

        nums[p1], nums[p2] = nums[p2], nums[p1]

        # Reverse numbers to the right of p1
        nums[p1 + 1:] = nums[p1 + 1:][::-1]
