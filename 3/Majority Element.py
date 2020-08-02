# Input: [2,2,1,1,1,2,2]
# Output: 2
from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
            if d[i] > len(nums) // 2:
                return i


Solution().majorityElement([3, 2, 3])
