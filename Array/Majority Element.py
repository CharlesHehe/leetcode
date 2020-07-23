from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >= 0:
            if nums.count(nums[-1]) <= len(nums) / 2:
                nums.remove(nums[-1])
            else:
                return nums[-1]

    # Runtime: 172 ms, faster than 75.58 %
    # Memory Usage: 15.1 MB, less than 84.86 %
    def majorityElement2(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]


if __name__ == "__main__":
    s = Solution()
    s.majorityElement(
        [3, 3, 4])