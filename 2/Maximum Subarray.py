# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        max_array = cur_array = nums[0]

        for n in nums:
            cur_array = max(cur_array + n, n)
            max_array = max(cur_array, max_array)
        return max_array


Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
