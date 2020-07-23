# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
from typing import List


class Solution:
    # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    def maxSubArray2(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(cur_sum, max_sum)
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        l = []
        for i in range(len(nums)):
            index = nums[i]
            l.append(index)
            for j in range(i + 1, len(nums)):
                index = index + nums[j]
                l.append(index)
        l.sort()
        return l[-1]


if __name__ == "__main__":
    s = Solution()
    s.maxSubArray2([-2, -1, -3, -4, -1, -2, -1, -5, -4])
