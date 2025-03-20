# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        if len(nums) == 1:
            return 1
        elif len(nums) == 2:
            return 2

        left = 0
        right = 0
        zero_count = 0
        one_count = 0
        max_consecutive_ones = 0

        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            else:
                one_count += 1

            if zero_count <= k:
                max_consecutive_ones = max(one_count + zero_count, max_consecutive_ones)

            elif zero_count > k:

                if nums[left] == 0:
                    zero_count -= 1
                else:
                    one_count -= 1

                left += 1

            right += 1


        return max_consecutive_ones
