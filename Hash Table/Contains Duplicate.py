# Input: [1,2,3,1]
# Output: true
from typing import List
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dic = defaultdict()
        dic = {}
        for i in nums:
            dic[i] = 1

        if len(dic) != len(nums):
            return True
        else:
            return False


if __name__ == "__main__":
    Solution().containsDuplicate([1, 2, 3, 1])