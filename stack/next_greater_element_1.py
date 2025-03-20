# https://leetcode.com/problems/next-greater-element-i/description/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        first_greater_dict = {}
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                index = stack.pop()
                first_greater_dict[nums2[index]] = nums2[i]

            stack.append(i)

        result = []
        for i in range(len(nums1)):
            if nums1[i] in first_greater_dict:
                result.append(first_greater_dict[nums1[i]])
            else:
                result.append(-1)

        return result
