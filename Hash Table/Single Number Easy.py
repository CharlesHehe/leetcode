# Given a non-empty array of integers, every element appears twice except for one.
# Find that single one.
#
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
from typing import List
from _collections import defaultdict


class Solution:

    # Runtime: 1712 ms, faster than 11.73 % Memory Usage: 16.5 MB, less than 10.92%
    def singleNumber(self, nums: List[int]) -> int:
        a = []
        for num in nums:
            if num not in a:
                a.append(num)
            else:
                a.remove(num)
        return a[0]

    # math
    def mathSingleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    def hashTableSingleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for num in nums:
            hash_table[num] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i


if __name__ == "__main__":
    s = Solution()
    s.hashTableSingleNumber([2, 2, 1])
