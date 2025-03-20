# https://leetcode.com/problems/next-greater-element-ii/

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        nums = nums + nums
        result = [-1] * len(nums)

        stack = []
        print(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]
            else:
                stack.append(i)

        return result[:len(nums) // 2]
