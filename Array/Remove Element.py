# Given an array nums and a value val, remove all instances of that value
# in-place and return the new length.
# Do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave
# beyond the new length.
# Example 1:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.
#
# It doesn't matter what you leave beyond the returned length.
from typing import List


class Solution:
    # not use remove
    def removeElement2(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count

    # remove
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in range(len(nums)):
            if nums[i - n] == val:
                nums.remove(nums[i - n])
                n = n + 1
        return len(nums)


if __name__ == "__main__":
    s = Solution()
    s.removeElement2(
        [3, 2, 2, 3], 2)
