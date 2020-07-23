from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_one = 0
        count_zero = 0
        count_two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            if nums[i] == 1:
                count_one += 1
            if nums[i] == 2:
                count_two += 1
        nums[:count_zero] = [0] * count_zero
        nums[count_zero:count_one + count_zero] = [1] * count_one
        nums[count_one + count_zero:count_two + count_one + count_zero] = [2] * count_two

        return None


Solution().sortColors([2, 0, 2, 1, 1, 0])