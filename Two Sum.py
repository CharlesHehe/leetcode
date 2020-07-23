from typing import List

# hash table to O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = nums.__len__()
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(nums):
            m = target - n
            if m not in h:
                h[n] = i
            else:
                return [h[m], i]


if __name__ == "__main__":
    s = Solution()
    # s.twoSum([2, 3, 4, 5], 7)
    s.twoSum2([2, 3, 4, 5], 7)
