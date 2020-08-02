# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        l = []
        for i, n in enumerate(numbers):
            if n in d:
                return [d[n], i + 1]
            d[target - n] = i + 1


Solution().twoSum([2,3,4], 6)
