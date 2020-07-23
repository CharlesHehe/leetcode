from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        for i in d:
            if d[i] > int(len(nums) / 2):
                return i


Solution().majorityElement([3, 2, 3])
