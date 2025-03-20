"""
Given an array, we need to find the next greater element for each element. If there is no greater element, we return -1.

Example Input: [4, 5, 2, 10, 8]

Expected Output: [5, 10, 10, -1, -1]
"""

from typing import List


def next_greater_elements(nums: List[int]) -> List[int]:

    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]

        stack.append(i)

    return result


if __name__ == "__main__":
    # Test the function
    nums = [4, 5, 2, 10, 8]
    print(next_greater_elements(nums))  # Output: [5, 10, 10, -1, -1]